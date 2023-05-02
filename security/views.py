from django.shortcuts import render,redirect
import sys
sys.path.append('..')
from core import AdvancedSecurity
from django.contrib import messages
import subprocess
import os
import sys

# Create your views here.

def GlobalLockDown(request):
    if request.method == 'POST':
        itemsDict = {}
        for key, value in request.POST.items():
            itemsDict[key] = value
        with open('LockdownKey.txt', 'r') as keyFile:
            if keyFile.read() == itemsDict['Key']:
                AdvancedSecurity.GLOBAL_LOCKDOWN = False
                AdvancedSecurity.GLOBAL_LOCKDOWN_KEY_SET = False
                AdvancedSecurity.flipSwitch()
                return redirect('login')


    return render(request,'GlobalLockDown.html')
