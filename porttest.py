#!/usr/bin/python3
# This code write by (Mr.nope)
import os
import time
class color:
      green = '\033[92m'
      blue = '\033[96m'
      red = '\033[91m'
      white = '\033[0m'
      End = '\033[0m'
porttest = "\nporttest/> "
ip = "\nEnter ip: "
port = "\nEnter port: "
packet = "\nEnter packet (1000/500/100/10/1): "
def cls():
    os.system("clear")
def start():
    os.system("clear")
    print(color.green + """
        _______  _______  _______ __________________ _______  _______ _________
        (  ____ )(  ___  )(  ____ )\__   __/\__   __/(  ____ \(  ____ \\__   __/
 	| (    )|| (   ) || (    )|   ) (      ) (   | (    \/| (    \/   ) (   
	| (____)|| |   | || (____)|   | |      | |   | (__    | (_____    | |   
	|  _____)| |   | ||     __)   | |      | |   |  __)   (_____  )   | |   
	| (      | |   | || (\ (      | |      | |   | (            ) |   | |  
	| )      | (___) || ) \ \__   | |      | |   | (____/\/\____) |   | |   
	|/       (_______)|/   \__/   )_(      )_(   (_______/\_______)   )_( """ + color.red + """" 
	                        (🅟🅞🅡🅣🅣🅔🅢🅣)""" + color.green + """
	                        [__ version 1.2.0          ]]]
	                        [- This code write by (Mr.nope)    -]
    	                        [-ms.nope github account : ---[    """+ color.red + """https://github.com/mrprogrammer2938/ ]]] """ + color.green + """
	                        [- usage 1 - and start package -----]""")
    print("\t1 - start portscan package")
    print("\t2 - Exit package... ")
    choose = input(porttest)
    if choose == '1':
      cls()
      print(color.green + """
   
   ████████████████████████████████████████████████
   █▄─▄▄─█─▄▄─█▄─▄▄▀█─▄─▄─█─▄─▄─█▄─▄▄─█─▄▄▄▄█─▄─▄─█
   ██─▄▄▄█─██─██─▄─▄███─█████─████─▄█▀█▄▄▄▄─███─███
   ▀▄▄▄▀▀▀▄▄▄▄▀▄▄▀▄▄▀▀▄▄▄▀▀▀▄▄▄▀▀▄▄▄▄▄▀▄▄▄▄▄▀▀▄▄▄▀▀""" + color.white)
      try1 = input(ip)
      time.sleep(1)
      print("\nip: " + try1 + color.green + " found!" + color.white)
      try2 = input(port)
      time.sleep(1)
      print("\nset port: " + color.green + try2 + color.white) 
      time.sleep(1)
      try3 = input(packet)
      time.sleep(1)
      print("\nset packet " + color.blue + try3)
      time.sleep(2)
      print(color.red + "---------------------------------------------------" + color.green)
      time.sleep(1)
      os.system("ping -w " + try3 + " " + try1 + " " + try2)
      print(color.red + "---------------------------------------------------" + color.white)
      time.sleep(1)
      trywork()
    elif choose == '2':
        ext()
    elif choose == '':
        start()
    elif choose == ' ':
        start()
    elif choose == '  ':
        start()
    else:
        os.system("clear")
        print(color.red + "Error porttest!" + color.white)
        time.sleep(2)
        try4 = input("\npress Enter... ")
        if try4 == '':
          start()
        else:
            start()
def trywork():
    tryworkopt = input("Do you want to try again? [y/n] ")
    if tryworkopt == 'y':
      startwork()
    elif tryworkopt == 'n':
        trymenu()
    else:
        trywork()
def ext():
    cls()
    print(color.green + "Exiting..." + color.End)
    exit()
def startwork():
    cls()
    print(color.green + """

   ████████████████████████████████████████████████
   █▄─▄▄─█─▄▄─█▄─▄▄▀█─▄─▄─█─▄─▄─█▄─▄▄─█─▄▄▄▄█─▄─▄─█
   ██─▄▄▄█─██─██─▄─▄███─█████─████─▄█▀█▄▄▄▄─███─███
   ▀▄▄▄▀▀▀▄▄▄▄▀▄▄▀▄▄▀▀▄▄▄▀▀▀▄▄▄▀▀▄▄▄▄▄▀▄▄▄▄▄▀▀▄▄▄▀▀""" + color.white)
    try1 = input(ip)
    time.sleep(1)
    print("\nip: " + try1 + color.green + " found!" + color.white)
    try2 = input(port)
    time.sleep(1) 
    print("\nset port: " + color.green + try2 + color.white)
    time.sleep(1)
    try3 = input(packet)
    time.sleep(1)
    print("\nset packet " + color.blue + try3)
    time.sleep(2)
    print(color.red + "---------------------------------------------------" + color.green)
    time.sleep(1)
    os.system("ping -w " + try3 + " " + try1 + " " + try2)
    print(color.red + "---------------------------------------------------" + color.white)
    time.sleep(1)
    trywork()
def trymenu():
    tryagain = input("Do you want to back mein menu [y/n] ")
    if tryagain == 'y':
      start()
    elif tryagain == 'n':
        ext()
    else:
        trymenu()
if __name__ == '__main__':
  try:
     start()
  except KeyboardInterrupt:
      print("\nCtrl + C")
      print("Exiting...")
      exit(1)
# porttest
