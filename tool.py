#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import time

# Renk tanımlamaları
R = "\033[1;31m"  # Kırmızı
G = "\033[1;32m"  # Yeşil
Y = "\033[1;33m"  # Sarı
B = "\033[1;34m"  # Mavi
C = "\033[1;36m"  # Cyan
W = "\033[1;37m"  # Beyaz
N = "\033[0m"     # Sıfırla

def banner():
    # Pydroid konsolunda çökme yapmaması için clear yerine alt alta boşluk bırakıldı
    print("\n" * 2)
    print(f"{C}=================================================={N}")
    print(f"{Y}          TERMUX OTOMATİK ARAÇ KURULUMU           {N}")
    print(f"{G}          Geliştirici: GitHub Uyumlu Script       {N}")
    print(f"{C}=================================================={N}\n")

def run_cmd(command):
    print(f"\n{B}[+] Çalıştırılıyor: {W}{command}{N}")
    status = os.system(command)
    if status != 0:
        print(f"{R}[!] İşlem sırasında bir hata oluştu veya komut yarıda kesildi.{N}")
    else:
        print(f"{G}[✔] İşlem başarıyla tamamlandı.{N}")
    input(f"\n{Y}Devam etmek için Enter tuşuna basın...{N}")

def update_system():
    print(f"{C}[*] Termux sistem paketleri güncelleniyor...{N}")
    run_cmd("pkg update -y && pkg upgrade -y")

def install_requirements():
    print(f"{C}[*] Temel bağımlılıklar yükleniyor...{N}")
    run_cmd("pkg install git python curl wget clang make libxml2 libxslt -y")

def install_toolx():
    print(f"{C}[*] Tool-X kuruluyor...{N}")
    cmd = "git clone https://github.com/Rajkumrdusad/Tool-X.git && cd Tool-X && chmod +x install.a && ./install.a"
    run_cmd(cmd)

def install_darkfly():
    print(f"{C}[*] DarkFly-Tool kuruluyor...{N}")
    cmd = "git clone https://github.com/SIIKAB/DarkFly-Tool.git && cd DarkFly-Tool && chmod +x install.sh && ./install.sh"
    run_cmd(cmd)

def install_lazymux():
    print(f"{C}[*] Lazymux kuruluyor...{N}")
    cmd = "git clone https://github.com/Gameye98/Lazymux.git && cd Lazymux && chmod +x lazymux.py && python3 lazymux.py"
    run_cmd(cmd)

def install_sqlmap():
    print(f"{C}[*] Sqlmap kuruluyor...{N}")
    run_cmd("git clone --depth 1 https://github.com/sqlmapproject/sqlmap.git")

def install_nmap():
    print(f"{C}[*] Nmap kuruluyor...{N}")
    run_cmd("pkg install nmap -y")

def main():
    while True:
        banner()
        print(f"{W}[1]{G} Sistem Güncelleme ve Temel Araçlar (Git, Python vb.)")
        print(f"{W}[2]{G} Tool-X Kur (Kali Linux Araç Yükleyicisi){N}")
        print(f"{W}[3]{G} DarkFly-Tool Kur{N}")
        print(f"{W}[4]{G} Lazymux Kur{N}")
        print(f"{W}[5]{G} Sqlmap Kur (SQL Açık Tarayıcı){N}")
        print(f"{W}[6]{G} Nmap Kur (Ağ Tarayıcı){N}")
        print(f"{W}[0]{R} Çıkış{N}")
        
        choice = input(f"\n{C}Seçiminiz ({W}0-6{C}): {N}").strip()
        
        if choice == '1':
            update_system()
        elif choice == '2':
            install_requirements()
            install_toolx()
        elif choice == '3':
            install_requirements()
            install_darkfly()
        elif choice == '4':
            install_requirements()
            install_lazymux()
        elif choice == '5':
            install_requirements()
            install_sqlmap()
        elif choice == '6':
            install_nmap()
        elif choice == '0':
            print(f"\n{Y}Çıkış yapılıyor. İyi günler!{N}")
            sys.exit(0)
        else:
            print(f"\n{R}[!] Geçersiz seçim, tekrar deneyin.{N}")
            time.sleep(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{Y}Program kullanıcı tarafından sonlandırıldı.{N}")
        sys.exit(0)
