# Infoga - Advanced Information Tool

## Description
Infoga is a tool for advanced information gathering on domains or hosts. It supports various features like pinging, Nmap scanning, Whois, brute force testing, and more.

## Features
- **Check Ping**: Tests the connection to a host.
- **Nmap**: Network scanning and port detection.
- **Whois**: Domain information.
- **Brute Force**: Tests credentials.
- **Detect APK**: Analyzes Android APK files.
- **Check Port**: Scans open ports.
- **NSLookup**: Retrieves DNS records.
- **Subdomain**: Finds subdomains.

## Requirements
- Python 3.x
- Required Tools:
  - `whois`
  - `nmap`
  - `sublist3r`

## Installation

### Windows Installation Package Use Chocolatey

To install on Windows, use the `.\install_windows_.ps1` script.

### Termux Installation Package Use Bash Script

`chmod +x install_termux.sh`
`./install_termux.sh`

### Linux Installation Package Use Bash Script

`sudo bash install_linux.sh`

### Run Program
1. Download or clone the repository:
   ```bash
   git clone https://github.com/Rixz-Ploit/scan.git

2. ```bash
   cd scan

3. ```bash
   python3 infoga.py
