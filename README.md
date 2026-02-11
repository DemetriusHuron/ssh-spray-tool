# 🐍 SSH Spray Tool

A lightweight, multi-threaded SSH Brute-Force and Password Spraying tool written in Python.
Designed for educational purposes and authorized security testing.

## 🚀 Features
- **Multi-threading support** (fast scanning).
- **Password Spraying:** Test one password against many users.
- **Brute-Force:** Test many passwords against one user.
- **Matrix Mode:** Test list of users against list of passwords.
- **Colorized Output:** Clean CLI interface.
- **Auto-save:** Successfully cracked credentials are saved to `hacked.txt`.

## 📦 Installation

1. Clone the repository:
```bash
   git clone https://github.com/DemetriusHuron/ssh-spray-tool.git
   cd ssh-spray-tool
```

2.   Install dependencies:

```bash
pip install -r requirements.txt
```

🛠 Usage

1. Brute-Force a single user

Target one specific user with a wordlist of passwords:
```bash
python3 ssh_spray.py <IP> -u admin -w passwords.txt
```
2. Password Spraying

Test a list of users against a password list:
```bash
python3 ssh_spray.py <IP> -U users.txt -w passwords.txt -t 20
```

Arguments
Flag	Description
target	Target IP address (e.g., 127.0.0.1)
-p, --port	Target port (Default: 22)
-u, --user	Single username to attack
-U, --userlist	File containing list of usernames
-w, --wordlist	File containing passwords
-t, --threads	Number of threads (Default: 10)

⚠️ Disclaimer

FOR EDUCATIONAL PURPOSES ONLY. This tool is intended for security research and testing systems you own or have explicit permission to test. The author is not responsible for any misuse or damage caused by this program.