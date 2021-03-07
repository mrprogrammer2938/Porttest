#!/usr/bin/python3
# This code write by (ms.nope)
import os
import time
class color:
    green = '\033[92m'
    blue = '\033[96m'
    red = '\033[91m'
    white = '\033[0m'
porttest = "\nporttest/> "
ip = "\nEnter ip: "
port = "\nEnter port: "
packet = "\nEnter packet (1000/500/100/10/1): "
time.sleep(1)
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
	                        [- This code write by (ms.nope)    -]
	                        [-ms.nope github account : ---[    """+ color.red + """https://github.com/msprogrammer2938/ ]]] """ + color.green + """
	                        [- usage 1 - and start package -----]""")
print("\t1 - start portscan package")
print("\t2 - Exit package... ")
choose = str(input(porttest))
if(str(choose) == '1'):
  time.sleep(1)
  os.system("clear")
  print(color.green + """
   
   ████████████████████████████████████████████████
   █▄─▄▄─█─▄▄─█▄─▄▄▀█─▄─▄─█─▄─▄─█▄─▄▄─█─▄▄▄▄█─▄─▄─█
   ██─▄▄▄█─██─██─▄─▄███─█████─████─▄█▀█▄▄▄▄─███─███
   ▀▄▄▄▀▀▀▄▄▄▄▀▄▄▀▄▄▀▀▄▄▄▀▀▀▄▄▄▀▀▄▄▄▄▄▀▄▄▄▄▄▀▀▄▄▄▀▀""" + color.white)
  try1 = str(input(ip))
  time.sleep(1)
  print("\nip: " + try1 + color.green + " found!" + color.white)
  try2 = str(input(port))
  time.sleep(1)
  print("\nset port: " + color.green + try2 + color.white) 
  time.sleep(1)
  try3 = str(input(packet))
  time.sleep(1)
  print("\nset packet " + color.blue + try3)
  time.sleep(2)
  print(color.red + "---------------------------------------------------" + color.green)
  time.sleep(1)
  os.system("ping -w " + try3 + " " + try1 + " " + try2)
  print(color.red + "---------------------------------------------------" + color.white)
  time.sleep(1)
  os.system("python3 1.py")
elif(str(choose) == '2'):
    time.sleep(1)
    os.system("clear")
    time.sleep(1)
    print("good bye")
    exit(1)
elif(str(choose) == ''):
    os.system("python3 porttest.py")
elif(str(choose) == ' '):
    os.system("python3 porttest.py")
else:
    time.sleep(1)
    os.system("clear")
    time.sleep(1)
    print(color.red + "Error porttest!" + color.white)
    time.sleep(2)
    try4 = str(input("press Enter... "))
    if(str(try4) == ''):
      os.system("python3 porttest.py")
    else:
        os.system("python3 porttest.py")
# porttest
