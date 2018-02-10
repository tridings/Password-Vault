#!/usr/bin/python

import os
import logging
from getpass import getpass
from bcrypt import hashpw, gensalt
import yaml

userAccountList = []

def account_check():
    username = raw_input(["Please enter username..."])
    if username in userAccountList:
        password = getpass.getpass(["Please enter password..."])
    else:
        print "username has not been registered..."
        print ""
        choice = raw_input(["Would you like to create and account? (yes/no)"])
        if choice == "yes":
            create_account(username)
        elif choice == "no":
            exit

def create_account(username):
    choice = raw_input(["Would you like to use the username you typed before? (yes/no)"])
    if choice == "yes":
        newUsername = username
    else:
        newUsername = raw_input(["Please enter new username..."])
    plaintext_password = getpass(["Please enter new password..."])
    hashed = hashpw(plaintext_password, gensalt())
    plaintext_password_check = getpass(["Please reenter new password..."])
    hashedCheck = hashpw(plaintext_password_check, gensalt())
    match = "no"
    while match == "no":
        if plaintext_password == plaintext_password_check:  
            print "Passwords match"
            userPassword = hashed
            userAccountList.append(newUsername)
            match = "yes"
            print userAccountList   
        else:
            print "Passwords do not match"
            match = "no"        

def main():
    account_check()

main()