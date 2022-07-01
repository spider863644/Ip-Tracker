#!/usr/bin/python 3
import os
import urllib.request, json
try:
   import colorama
except:
    os.system("pip install colorama")
try:
    import pyfiglet
except:
    os.system("pip install pyfiglet")
from colorama import *
auth = '1840e53e-0a8b-4d4d-b4e6-4d34d1033d91';
import time as t
t.sleep(2)
os.system("clear")
def loop():
    head = pyfiglet.figlet_format("Ip - Tracker")
    os.system("clear")
    print(Fore.GREEN + head)
    print(Fore.YELLOW + """
    [+]Tool Name:Ip Tracker
    [+]Creator:Spider Anongreyhat
    [+]Team:Termuxhackz Society
    [+]Whatsapp:+2349052863644
    [+]Github:https://github.com/spider863644
    [+]Credit goes to AnonyminHack5
    [+]Version: V1.1.0""")
    print(Fore.BLUE + """ ============================================""")
    #print("Usage:Iptracker [Ip address]\n\nExample:Iptracker 192.168.1.95")
    print(Fore.GREEN + """
    Type \"show\" to show all command 
    
    """)
    def track():
        tip = input(Fore.MAGENTA + "Iptracker > " + Style.RESET_ALL)
        if tip == "help":
            print(Fore.BLUE + """
            show :  Its Display all commands
            iptracker :  This is used for tracking an Ip address
            help :  Its display how to use this tool
            exit : For quitting ip tracker
            
            update:  Its update Ip-Tracker automatically 
            """)
            track()
        elif tip == "show":
            print(Fore.BLUE + """
            This are the available commands
            help
            show
            exit
            iptracker
            update
            """)
            track()
        elif tip == "exit":
            print(Fore.YELLOW + "Thanks for using my tool\nIf you find any error,donot hestitate to message me on whatsapp")
            exit()
        elif tip == "iptracker":
            print(Fore.GREEN + """________________________________Track Ip____________________________""")
            print("""
            """)
            
            ip = (input(Fore.YELLOW + Back. RED + "Enter IP Address : " + Style.RESET_ALL + ""))
            url = 'https://ipfind.co/?auth=' + auth + '&ip=' + ip;
            try:
                response = urllib.request.urlopen(url)
                print(Fore.CYAN + " Fetching data from " + ip)
                t. sleep(2)
                data = json.loads(response.read())
                print(Fore.YELLOW,  data)
            except:
                print(Fore.RED + "Invalid IP address")
                t. sleep(2)
                loop()
        elif tip == "update":
            print(Fore.GREEN + "Updating Ip Tracker")
            os.system("""
            cd
            rm -f -r Ip-Tracker
            git clone https://github.com/spider863644/Ip-Tracker
            """)
            print(Fore.BLUE + """Now type the following command
            cd $HOME
            cd Ip-Tracker
            python3 tracker.py
            """)
        else:
            print(Fore.RED + "Invalid Command!")
            t.sleep(3)
            track()
    track()
            
    cont = input(Fore.YELLOW + Back. RED + "Would you like to track another IP address? [y/n] " + Style.RESET_ALL + " ")
    if cont == "y" or cont == "Y":
        loop()
    else:
        exit()
loop()