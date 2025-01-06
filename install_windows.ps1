# Memastikan bahwa Chocolatey sudah terinstal
if (-Not (Get-Command choco -ErrorAction SilentlyContinue)) {
    Write-Host "Chocolatey belum terinstal. Menginstal Chocolatey..."
    Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.SecurityProtocolType]::Tls12; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
    Write-Host "Chocolatey berhasil diinstal."
}

# Memperbarui Chocolatey
Write-Host "Memperbarui Chocolatey..."
choco upgrade chocolatey -y
sleep 2

# Menginstal Paket Whois
Write-Host "Menginstal Paket Whois..."
choco install whois -y
sleep 2

# Menginstal Paket Nmap
Write-Host "Menginstal Paket Nmap..."
choco install nmap -y
sleep 2

# Menginstal Paket Nslookup
Write-Host "Menginstal Paket Nslookup..."
choco install dnsutils -y
sleep 2

# Menginstal Paket Python dan Pip
Write-Host "Menginstal Paket Python dan Pip..."
choco install python -y
sleep 2

# Menginstal Sublist3r dengan Pip
Write-Host "Menginstal Sublist3r menggunakan Pip..."
python -m pip install sublist3r
sleep 2

Write-Host "`nSUKSES INSTALL SEMUA PAKET DI WINDOWS!"
