#!/data/data/com.termux/files/usr/bin/bash

echo -e "Mengupdate Repositori..."
pkg update -y
pkg upgrade -y
sleep 2

echo -e "\nMenginstall Paket Whois..."
pkg install -y whois
sleep 2

echo -e "\nMenginstall Paket Nmap..."
pkg install -y nmap
sleep 2

echo -e "\nMenginstall Paket Nslookup..."
pkg install -y dnsutils
sleep 2

echo -e "\nMenginstall Paket Python dan Pip..."
pkg install -y python python-pip
sleep 2

echo -e "\nMenginstall Sublist3r dengan Pip..."
pip install sublist3r
sleep 2

echo -e "\n\nSUKSES INSTALL SEMUA PAKET\nSIAPKAN SCRIPT PYTHON UNTUK DIGUNAKAN!"
