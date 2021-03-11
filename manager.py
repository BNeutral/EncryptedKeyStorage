#!/usr/bin/env python
# -*- coding: utf-8 -*-
from getpass import getpass
import pyscrypt
import json

password = None
entries = {}
filename = "keys"
loopMenu = True

def inputPassword():
    global password
    global entries
    print("Enter password:")
    password = getpass().encode()
    data = getData()
    print(data)
    print("Does this decoding look correct? y/n")
    if input() == "y":
        if data != b"":
            entries = json.loads(data)

def getData():
    data = bytearray()
    try:
        with pyscrypt.ScryptFile(filename, password) as f:
            data = f.read()
    finally:
        return data

def addEntry():
    if password == None:
        print("Set up the password first!")
        return
    global entries
    print("Input key:")
    key = input()
    print("Input val:")
    val = input()
    print("Does this look correct? y/n")
    print(key,val)
    if input() == "y":
        entries[key] = val

def save():
    if password == None:
        print("Set up the password first!")
        return
    with pyscrypt.ScryptFile(filename, password, 1024, 1, 1) as f:
        
        f.write(json.dumps(entries).encode())

def leave():
    global loopMenu
    loopMenu = False

def printData():
    for key,value in entries.items():
        print(key+": "+value)

def main():
    menuChoices = {1 : inputPassword, 2 : addEntry, 3 : printData, 4 : save, 5 : leave}
    choice = None
    while loopMenu:
        print("\nMenu:")
        print(menuChoices)
        print("")
        choice = int(input())
        menuChoices[choice]()

main()