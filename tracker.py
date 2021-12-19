#!/usr/bin/python 3
import os
import time as t
t.sleep(3)
os.system("clear")
os.system("""apt update && apt install figlet
clear""")

def loop():
    os.system("clear")
    os.system("figlet Ip-Tracker")
    print("""
    [+]Tool Name:Ip Tracker
    [+]Creator:Spider Anongreyhat
    [+]Team:Termuxhackz Society
    [+]Whatsapp:+2349052863644
    [+]Github:https://github.com/spider863644
    [+]  Credit goes to anonyminhack5""")
    print(""" ============================================""")
    #print("Usage:Iptracker [Ip address]\n\nExample:Iptracker 192.168.1.95")
    print("""
    Type \"show\" to show all command 
    
    """)
    def track():
        tip = input("Iptracker> ")
        if tip == "help":
            print("""
            show :  Its Display all commands
            iptracker :  This is used for tracking an Ip address
            help :  Its display how to use this tool
            exit : For quitting ip tracker
            
            update:  Its update Ip-Tracker automatically 
            """)
            track()
        elif tip == "show":
            print("""
            This are the available commands
            help
            show
            exit
            iptracker
            update
            """)
            track()
        elif tip == "exit":
            print("Thanks for using my tool\nIf you find any error,donot hestitate to message me on whatsapp")
            exit()
        elif tip == "iptracker":
            print("""________________________________Track Ip____________________________""")
            print("""Choose an Operating system you are using for ip tracker
            [1]Linux
            [2]Termux
            """)
            oos = input("iptracker> ")
            if oos == "1":
                os.system("sudo apt install w3m")
            elif oos == "2":
                os.system("apt install w3m")
            else:
                print("U choose an Invalid Operating system\nChoosing termux as a default Operating System")
                os.system("apt install w3m")
            ip = (input("Enter IP Address "))
            url = "w3m https://www.melissa.com/v2/lookups/iplocation/ip/?ip=" + ip + "&site="
            os.system(url)
            
        elif tip == "update":
            print("Updating Ip Tracker")
            os.system("""
            cd
            rm -f -r Ip-Tracker
            git clone https://github.com/spider863644/Ip-Tracker
            """)
            print("""Now type the following command
            cd $HOME
            cd Ip-Tracker
            python3 tracker.py
            """)
        else:
            print("Invalid Command!")
            t.sleep(5)
            print("")
            track()
    track()
            
    cont = input("Would you like to track another IP address? [y/n] ")
    if cont == "y" or cont == "Y":
        loop()
    else:
        exit()
loop()