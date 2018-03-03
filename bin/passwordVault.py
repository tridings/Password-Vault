#!/usr/bin/python

import os
import logging
from getpass import getpass
from bcrypt import hashpw, gensalt
import yaml

userAccountList = []
accountTypes = []

with open("/home/mint/scripts/python/etc/myYamlFile.yaml") as f:
    list_doc = yaml.load(f)

def account_authenticate():
    username = raw_input(["Please enter username..."])
    if username in userAccountList:
        password = getpass.getpass(["Please enter password..."])
        hashedPassword = hashpw(password, gensalt())
        if hashedPassword == list_doc[username]["password"]:
            return True
            # This should probably be a new function

        else:
            print "Incorrect Password"
            return False
            exit
    else:
        print "Username has not been registered..."
        print ""
        choice = raw_input(["Would you like to create and account? (yes/no)"])
        if choice == "yes":
            create_account(username)
        elif choice == "no":
            exit

def process_request():
    if account_authenticate() == True:
        option = raw_input(["Please enter one of these account passwords that you'd like : %s" % accountTypes])
        retrievedPassword = list_doc[option]['password']
        addToClipBoard(retrievedPassword)

def addToClipBoard(text):
    command = 'echo ' + text.strip() + '| clip'
    os.system(command)

def create_account(username):
    choice = raw_input(["Would you like to use the username you typed before? (yes/no)"])
    if choice == "yes":
        newUsername = username
    else:
        newUsername = raw_input(["Please enter new username..."])
    plaintext_password = getpass(["Please enter new password..."])
    salt = gensalt()
    hashed = hashpw(plaintext_password, salt)
    plaintext_password_check = getpass(["Please reenter new password..."])
    hashedCheck = hashpw(plaintext_password_check, salt)
    # match = "no"
    # while match == "no":
    if hashed == hashedCheck:  
        print "Passwords match"
        userPassword = hashed
        userAccountList.append(newUsername)
        list_doc[newUsername]['password'] = hashed
        match = "yes"
        print userAccountList   
    else:
        print "Passwords do not match"
        match = "no" 
        exit       

def main():
    account_authenticate()

main()