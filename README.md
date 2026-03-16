# 🔎 Python Port Scanner

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Nmap](https://img.shields.io/badge/Nmap-Scanner-green)
![Status](https://img.shields.io/badge/Status-Active-success)

```
______          _     _____
| ___ \        | |   /  ___|
| |_/ /__  _ __| |_  \ `--.  ___ __ _ _ __  _ __   ___ _ __ 
|  __/ _ \| '__| __|  `--. \/ __/ _` | '_ \| '_ \ / _ \ '__|
| | | (_) | |  | |_  /\__/ / (_| (_| | | | | | | |  __/ |   
\_|  \___/|_|   \__| \____/ \___\__,_|_| |_|_| |_|\___|_|   

Author: Erica Almeida
Simple Nmap Automation Tool
----------------------------------
Enter target IP or domain: 45.33.32.156

Scanning target 45.33.32.156 ... please wait

Scan Results
----------------------------------
Hosts found: 1
Host: 45.33.32.156 (scanme.nmap.org)
State: up
Protocol: tcp
Port: 22 | State: open | Service: ssh | Version: OpenSSH 6.6.1p1 Ubuntu 2ubuntu2.13
Port: 25 | State: filtered | Service: smtp | Version:
Port: 80 | State: open | Service: http | Version: Apache httpd 2.4.7

TXT results saved to results/scan_2026-03-16_00-47-36.txt
JSON results saved to results/scan_2026-03-16_00-47-36.json

Scan completed successfully.
```

# 📖 Description

This project is a simple port scanner automation tool built with Python and Nmap.
It allows users to scan a target IP address or domain and identify open ports, running services, and service versions.

The tool automates the execution of Nmap scans using the Python library python-nmap, displaying results in 
the terminal and saving them in both TXT and JSON formats for further analysis.

This project was developed to practice:

- Network scanning concepts
- Python automation
- Cybersecurity fundamentals
- Interaction with external tools (Nmap)
- Structured result storage

The generated results help with basic network enumeration, which is a common task in cybersecurity assessments and penetration testing.

# ⚙️ Technologies Used

- Python 3
- Nmap
- python-nmap
- pyfiglet
- Python Standard Library (os, json, datetime)

# 📂 Project Structure

```
port-scanner/
|
├── scanner.py
├── requirements.txt
└── results/
    ├── scan_2026-03-16_00-47-36.json
    └── scan_2026-03-16_00-47-36.txt 
```
- scanner.py: Main script responsible for executing the scan and processing the results.
- requirements.txt: Contains the Python dependencies required to run the project.
- results/: Directory where scan results are automatically saved.

# 📋 Prerequisites

Before running the project, make sure you have the following installed:

- Python 3.8+
- Nmap

## Install Nmap:

### Linux
```bash
sudo apt install nmap
```
### Windows

Download from the official website:  
[Nmap Official Download](https://nmap.org/download.html)

# 📦 Installation

1️⃣ Clone the repository
```bash
git clone https://github.com/yourusername/port-scanner.git
```
2️⃣ Navigate to the project directory
```bash
cd port-scanner
```
3️⃣ Install Python dependencies
```bash
pip install -r requirements.txt
```

# 🚀 Usage

Run the scanner using:
```bash
python scanner.py
```

Then enter the target IP address or domain when prompted.

Example:
```
Enter target IP or domain: scanme.nmap.org
```

The script will execute an Nmap scan with the following options:
```
-sV  -> Detect service versions
-sC  -> Run default Nmap scripts
```

## 📊 Output Files

### TXT

Human-readable scan results.

Example:
```
Host: 45.33.32.156
State: up
Protocol: tcp
Port: 22 | State: open | Service: ssh | Version: OpenSSH 7.9
```

### JSON

Structured results for automation or further processing.

Example:
```
{
    "target": "scanme.nmap.org",
    "scan_time": "2026-03-16_00-47-36",
    "hosts": {}
}
```

# ⚠️ Disclaimer

This tool is intended for educational purposes only.
Only scan systems you own or have explicit permission to test.
Unauthorized scanning may violate laws and regulations.

# 👩‍💻 Author

Erica Almeida

Computer Engineering Student | Cybersecurity and Networking Enthusiast
