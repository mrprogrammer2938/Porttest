#!/usr/bin/python3
# This code write by (ms.nope)
import os
import time
class color:
    red = '\033[91m'
    white = '\033[0m'
try1 = str(input("Do you want to try again? [y/n] "))
if(str(try1) == 'y'):
  os.system("python3 porttest.py")
elif(str(try1) == 'n'):
    time.sleep(1)
    os.system("clear")
    time.sleep(1)
    print("good bye")
    exit(1)
elif(str(try1) == ''):
    os.system("python3 1.py")
elif(str(try1) == ' '):
    os.system("python3 1.py")
else:
    time.sleep(1)
    os.system("clear")
    print(color.red + "Error porttest!" + color.white)
    time.sleep(2)
    try2 = str(input("press Enter... "))
    if(str(try2) == ''):
      os.system("clear")
      os.system("python3 1.py")
    else:
        os.system("clear")
        os.system("python3 1.py")
# porttest
