#export PYTHONPATH="test"
import sys
import os
from datetime import datetime
from . import AdvancedSecurity
from django.shortcuts import redirect
path = os.path.abspath("module1")
sys.path.append(path)
print(path)

GLOBAL_LOGIN_ATTEMPT = {}
MASTER_FAILED_LOGGING = 0

def LogLogin(REMOTE_ADDR,USER_NAME,CALLED_FROM):
    #self.request.META.get('REMOTE_ADDR')
    #form.get_user
    with open("LoginLogs.txt", 'a') as LogingLogFile:
        addon = "LOGIN ATTEMPT"


        if CALLED_FROM == "success":
            if GLOBAL_LOGIN_ATTEMPT.get(str(USER_NAME)) == None:
                GLOBAL_LOGIN_ATTEMPT[str(USER_NAME)] = 0
            else:
                GLOBAL_LOGIN_ATTEMPT[str(USER_NAME)] = 0
            addon = "LOGIN SUCCESS"



        if GLOBAL_LOGIN_ATTEMPT.get(str(USER_NAME)) == None:
            GLOBAL_LOGIN_ATTEMPT[str(USER_NAME)] = 1
        else:
            GLOBAL_LOGIN_ATTEMPT[str(USER_NAME)] += 1

        string = datetime.now().strftime("%m/%d/%Y %H:%M:%S")+" || "+str(REMOTE_ADDR)+" || "+str(USER_NAME)+ " || "+addon+"\n"
        LogingLogFile.write(string)
        if GLOBAL_LOGIN_ATTEMPT.get(str(USER_NAME)) >= 2 :
            #"Administer Global Lockdown"
            print("Administer Global Lockdown")
            AdvancedSecurity.administerLockdown()
            #AdvancedSecurity.GLOBAL_LOCKDOWN = True
            #last here on 31/03/2023
