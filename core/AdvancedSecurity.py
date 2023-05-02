import sys
import os
import random
import string
import subprocess
from django.shortcuts import redirect
import importlib
from django.conf import settings
from django.urls import conf
from django.urls import utils,clear_url_caches,clear_script_prefix
# Reload urls.py module
#from . import LockDown
path = os.path.abspath("module1")
sys.path.append(path)
#print(path)
import sys


#GLOBAL_LOCKDOWN = False
#LOBAL_LOCKDOWN_KEY_SET = False

GLOBAL_SWITCH_BOARD = open(r"GLOBAL_SWITCH_BOARD.txt",'r')
SWITCH_DATA = GLOBAL_SWITCH_BOARD.read()
SWITCH_DATA = SWITCH_DATA.split("\n")
SWITCH_DATA = SWITCH_DATA[1].split(",")
GLOBAL_LOCKDOWN = False if SWITCH_DATA[0] == 'F' else True
GLOBAL_LOCKDOWN_KEY_SET = False if SWITCH_DATA[1] == 'F' else True
GLOBAL_SWITCH_BOARD.close()



standard_first_line = "GLOBAL_LOCKDOWN,GLOBAL_KEY_SET,GLOBAL_LICENSE_SET\n"

def flipSwitch():
    stringBuild = ""
    if GLOBAL_LOCKDOWN == True:
        stringBuild += 'T,'
    else:
        stringBuild += 'F,'
    if GLOBAL_LOCKDOWN_KEY_SET == True:
        stringBuild += 'T,F'
    else:
        stringBuild += 'F,F'

    finalString = standard_first_line+stringBuild
    with open(r"GLOBAL_SWITCH_BOARD.txt",'w') as file:
        print(finalString)
        file.write(finalString)
        file.close()


def administerLockdown():
    global GLOBAL_LOCKDOWN,GLOBAL_LOCKDOWN_KEY_SET
    print(GLOBAL_LOCKDOWN)
    GLOBAL_LOCKDOWN = True
    if GLOBAL_LOCKDOWN_KEY_SET == False:
        with open("LockdownKey.txt", 'w') as LockdownKey:
            pool = string.ascii_letters + string.digits
            key = ''.join(random.choice(pool) for i in range(128))
            LockdownKey.write(key)
            LockdownKey.close()
            GLOBAL_LOCKDOWN_KEY_SET = True


    flipSwitch()








