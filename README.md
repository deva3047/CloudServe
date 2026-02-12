# 🚀 SERVER – Easy Cloudflared Web Server Tool

**Version:** 1.0  
**Author:** Jay Joshi  

SERVER is a lightweight and easy-to-use tool that allows you to create a local Apache web server and instantly expose it to the internet using **Cloudflared Tunnel** — without any port forwarding.

It is designed for **learning, testing, demo hosting, and secure local sharing**.

---

## ✨ Features

### 🔧 Server Management
- Auto install Apache2  
- Start / Stop server  
- Live server status  
- Enable directory listing  
- Open server in browser  

### 🌍 Public Access
- Generate Cloudflared public URL  
- No port forwarding required  
- Works behind NAT / firewall  

### 📁 File Management
- Upload files  
- Delete files  
- List uploaded files  
- Show file size & upload time  

### 📊 Visitor Logging
- Visitor IP address  
- Browser name  
- User-Agent  
- Access time  
- Requested file  

### 🧠 System Information
- Operating system  
- Logged-in user  
- CPU cores  
- RAM usage  
- Disk space  

---

## 💻 Supported Operating Systems
- Kali Linux  
- Ubuntu  
- Debian  
- WSL (Windows Subsystem for Linux)

---

## 📦 Requirements

Make sure these are installed:

```bash
apache2
curl
wget
unzip
cloudflared
python3



⚙ kali Installation

git clone https://github.com/deva3047/CloudServe.git
cd SERVER
python server.py



⚙ Termux Installation

pkg update && pkg upgrade
git clone https://github.com/deva3047/CloudServe.git
cd SERVER
python3 server.py



▶ Usage
python server.py

Choose options from the interactive menu:

Start server

Stop server

Upload files

Generate public link

View logs

View system info





📂 Default Paths
| Item          | Path                     |
| ------------- | ------------------------ |
| Web root      | `/var/www/html/`         |
| Upload folder | `/var/www/html/uploads/` |
| Logs          | `logs/visitors.log`      |






🔐 Security Notes (Important)

This tool exposes your local server to the internet.

Please follow these rules:

Do not upload sensitive files

Restrict upload file types

Do not use on production servers

Anyone with the link can access your server

Logs contain real IP addresses





📜 License 
MIT License
You are free to use, modify and distribute this software.






🧑‍💻 Author

Jay Joshi
Cyber Security Student
GitHub: https://github.com/deva3047






⚠ Disclaimer

This tool is made for educational and testing purposes only.

The author is not responsible for:

Illegal hosting

Data misuse

Unauthorized access

Security incidents

Use responsibly.



Starting Server...
[██████████] 100%
