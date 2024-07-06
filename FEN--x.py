import os
from colorama import Fore, Style, init

init()
os.system("pip3 install nmap")
os.system("clear")
print(Fore.CYAN + "")
os.system("figlet script")
print(Fore.RED + "HEDEF SİTE GİR")
print("----------------------------")
islemno = input("root@FEN-ıx:~ ")

def script(islemno):
    print(Fore.MAGENTA + "")
    os.system(f"nmap --script all {islemno}")

script(islemno)
print(Style.RESET_ALL)
