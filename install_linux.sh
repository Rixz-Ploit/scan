#!/bin/bash

echo -e "Mengupdate Repositori..."
sudo apt update -y
sudo apt upgrade -y
sleep 2

echo -e "\nMenginstall Paket Whois..."
sudo apt install -y whois
sleep 2

echo -e "\nMenginstall Paket Nmap..."
sudo apt install -y nmap
sleep 2

echo -e "\nMenginstall Paket Nslookup..."
sudo apt install -y dnsutils
sleep 2

echo -e "\nMenginstall Paket Python dan Pip..."
sudo apt install -y python3 python3-pip
sleep 2

echo -e "\nMenginstall Sublist3r dengan Pip..."
pip3 install sublist3r
sleep 2

echo -e "\n\nSUKSES INSTALL SEMUA PAKET\nSIAPKAN SCRIPT PYTHON UNTUK DIGUNAKAN!"
