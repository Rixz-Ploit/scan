import os
import time
import sys
from datetime import datetime

#variable color
Bl='\033[30m'
Re='\033[1;31m'
Gr='\033[1;32m'
Ye='\033[1;33m'
Blu='\033[1;34m'
Mage='\033[1;35m'
Cy='\033[1;36m'
Wh='\033[1;37m'

#whois
def whois() :
     print(f"\n{Cy}[•]====== {Re}Wois Web : {domain} {Cy}======[•]{Gr}")
     os.system(f"whois {domain}")

#nmap
def nmap() :
    print(f"\n{Cy}[•]==== {Re}Scan Nmap Web : {domain} {Cy}====[•]{Gr}")
    os.system(f"nmap {domain}")
    
#nslookup
def nslu() :
    print(f"\n{Cy}[•]==== {Re}Nslookup Web : {domain} {Cy}====[•]{Gr}")
    os.system(f"nslookup {domain}")    
    
#brute force
def brute() :
    print(f"\n{Cy}[•]=== {Re}Brute Force Web : {domain} {Cy}===[•]{Gr}")
    os.system(f"nmap --script ssh-brute -p22 {domain}")
    os.system(f"nmap --script ftp-brute -p21 {domain}")
    
#detec apk
def apk() :
    print(f"\n{Cy}[•]==== {Re}Detec Apk Web : {domain} {Cy}====[•]{Gr}")
    os.system(f"nmap -O {domain}")
    
#port scanner
def port() :
    print(f"{Cy}[•]=== {Re}Port Scanner Web : {domain} {Cy}===[•]{Gr}")
    os.system(f"nmap -p 1-500 {domain}")  
    
#subdomain
def sub() :
    print(f"\n{Cy}[•]==== {Re}Subdomain Web : {domain} {Cy}====[•]{Gr}")
    os.system(f"sublist3r -d {domain}")                   

#cek ping
def cek_ping():
    print(f"\n{Cy}[•]==== {Re}Check Ping Web : {domain} {Cy}====[•]{Gr}")
    os.system(f"ping -c 4 {domain}")  #

#pilih
def pil() :
    pilih = input(f"\n{Cy}Scan Again?? y/n :")
    
    if pilih == "y" :
        os.system("python3 infoga.py")
    elif pilih == "n" :
        print(f"{Re} Exit.....")
        time.sleep(1)
        sys.exit       
    else :
            print("Choose y or n")
            pil()
            
#banner
def banner() :
    print(f"""
    {Blu}
    ██████╗░██████╗░░█████╗░░██████╗░████████╗███████╗██████╗░
    ██╔══██╗██╔══██╗██╔══██╗██╔════╝░╚══██╔══╝██╔════╝██╔══██╗
    ██║░░██║██████╔╝███████║██║░░██╗░░░░██║░░░█████╗░░██████╔╝
    ██║░░██║██╔══██╗██╔══██║██║░░╚██╗░░░██║░░░██╔══╝░░██╔══██╗
    ██████╔╝██║░░██║██║░░██║╚██████╔╝░░░██║░░░███████╗██║░░██║
    ╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝░╚═════╝░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝
                                                         

   {Cy} ----------------------------------------------------------
                  Advanced Information Tool
                  Code By : Rixz-Ploit
                  Github : github.com/Rixz-Ploit
                  Date : {datetime.now()}
  {Cy}  ----------------------------------------------------------{Ye}

    [1] Check Ping         - Check ping host.
    [2] Nmap               - Network scanning & port detection.
    [3] Whois              - Domain information lookup.
    [4] Brute Force        - Test credentials.
    [5] Detect APK         - Scan Android APK files.
    [6] Check Port Nmap    - Check open ports with Nmap.
    [7] NSLookup           - Retrieve DNS records of a domain.
    [8] Subdomain          - Discover subdomains of a domain.

   {Cy} ----------------------------------------------------------{Wh}""")

    
os.system("clear")            
banner()    
domain = input(f"\n{Cy}Input Target Example({Re}example.com{Cy}) :")

os.system("clear")
print("Loading....")
time.sleep(1)
cek_ping()
time.sleep(0.5)
nmap()
time.sleep(0.5)
whois()
time.sleep(0.5)
brute()
time.sleep(0.5)
apk()
time.sleep(0.5)
port()
time.sleep(0.5)
nslu()
time.sleep(0.5)
sub()
time.sleep(0.5)
pil()



    