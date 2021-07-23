#!/usr/bin/python3
# This Code Write by Mr.nope
# Calendar 1.3

import calendar
import datetime
import os
import subprocess
import time
import sys
import platform
try:
    from colorama import Fore,init
    init()
except ImportError:
    os.system("pip3 install colorama")

system = platform.uname()[0]
End = '\033[0m'
run_Err = "\nPlease, Run This Programm on Linux, MacOS!\n"
opt = Fore.GREEN + "\nCalendar/> " + End
banner = Fore.GREEN + """
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWNNNNNNWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNKkdollccccccclodkKNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWXkoc:codkO0kdok0Okxoc::lkXWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM """ + Fore.RED + 'Version: ' + Fore.CYAN + "1.3" + Fore.GREEN +"""
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMWKo::odx0NWWWWk,'dNWWWWXkdo:;o0WMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMKo;cxKN0cc0WWWWKxdONWWWXl;kNXkc;lKWMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMWO:;xXNWWW0x0WWWWWWWWWWWWKxkNWWWNk;;kWMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMWx,ckkOXWWWWWWWWWWWWWWWWWWWWWWWWN0OOc'dNMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMWk,c0KdcoKWWWWWWWWWWWWWWWWWWWWKko::l0Kl'xWMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMK:;ONWWXKNNOod0NWWWWWWWWWWN0dc::lx0NWW0;;0MMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMk,lXWWWWWWWXklccokKNWWNKko::cdOXNNWWWWNd'dWMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMWo'dKkxkXWWWWWWXOoc:cloc::lx0XNNWWWXOxkKk'lWMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMWo'x0dld0WWWWWWWWWN0xllokKXNWWWWWWWKdlo0k'lNMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMx'oNWWWWWWWWWWWWWWWWNNNNNWWWWWWWWWWWWWWd'dWMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMK:;0WWWWNWWWWWWWWWWWWWWWWWWWWWWWWNNWWWX:,0MMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMWx,lXXklo0WWWWWWWWWWWWWWWWWNNWWWKdcdXNo'dWMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMNd,l0xdOXWWWWWWWWWWWWWWWWWNNNWWN0ddOo'oNMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMNx,cONWWWWXOKWWWWWWWWWWWWXOKNWWWN0c,dNMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMW0c,o0NWKc;kNWWWXOkKNWWW0:;ONNKo;:OWMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMNOc;cxkdkXNNWNx'.oNWNNN0dxxl;ckNMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMW0dc:coxO0KX0dokXX0Odoc:cd0WMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWXOdlcccccccccccclokKWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNXKKKKKKXNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM""" + End

def ext():
    os.system("clear")
    print(Fore.GREEN + 'Exiting...' + End)
def main():
    if system == 'Windows':
        print(run_Err)
        sys.exit()
    elif system == 'Linux':
        menu()
    else:
        print(run_Err)
        sys.exit()
def start_time():
    os.system("clear")
    run_1 = datetime.datetime.now()
    print(run_1)
    try1()
def start_date():
    os.system("clear")
    year = 2021
    mo = int(input("\nEnter month: "))
    print("\n")
    print(calendar.month(year,mo))
    try1()
def start_weather():
    os.system("clear")
    city = input("\nEnter City: ")
    time.sleep(1)
    run_2 = subprocess.getoutput(f"curl -s http://wttr.in/{city}")
    print(run_2)
    try1()
def start():
    os.system("clear")
    print("\nUsage: Ctrl + D To Back Main Menu!\n")
    time.sleep(0.50)
    run_1 = datetime.datetime.now()
    print('Date: ' + str(run_1))
    print("\n")
    year = 2021
    mo = int(input("\nEnter month: "))
    print('\n')
    print(calendar.month(year,mo))
    print('\n')
    city = input("\nEnter City: ")
    time.sleep(1)
    run_2 = subprocess.getoutput(f"curl -s http://wttr.in/{city}")
    print(run_2 + "\n")
    try1()
def list():
    print("\n{1}.Time")
    print("{2}.Date")
    print("{3}.weather")
    print("{4}.All")
    print("{99}.Exit")
    choose = input(opt)
    if choose == '1':
        start_time()
    elif choose == '2':
        start_date()
    elif choose == '3':
        start_weather()
    elif choose == '4':
        start()
    elif choose == '99':
        ext()
    else:
        main()
def menu():
    os.system("printf '\033]2;Calendar\a'")
    os.system("clear")
    print(banner)
    list()
def try1():
    try_to_Main_menu = input("\npress Enter...")
    if try_to_Main_menu == '':
        main()
    else:
        main()
if __name__ == '__main__':
    try:
        try:
            main()
        except KeyboardInterrupt:
            print("\nCtrl + C")
            print("\nExiting...")
            sys.exit()
    except EOFError:
        try1()