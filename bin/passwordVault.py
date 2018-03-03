#!/usr/bin/python

import os
import logging
from getpass import getpass
from bcrypt import hashpw, gensalt
import yaml

userAccountList = []
filePath = "/home/mint/scripts/python/etc/myYamlFile.yaml"

def yaml_loader(filepath):
    # Loads a yaml file
    with open (filepath, "r") as file_descriptor:
        data = yaml.load(file_descriptor)
    return data

def yaml_query(filepath, request):
    queryResult = yaml_loader(filepath)[request]
    return queryResult

def yaml_dump(filepath, data):
    # Dumps data to a yaml file
    with open(filepath, "w") as file_descriptor:
        yaml.dump(data, file_descriptor)

def account_authenticate():
    record= yaml_loader(filePath)
    username = raw_input(["Please enter username..."])
    # This needs to check against the yaml file "accounts" to see if it exists
    if username in record['accounts']:
        password = getpass(["Please enter password..."])
        hashedPassword = hashpw(password, record['accounts'][username]['salt'])
        if hashedPassword == record['accounts'][username]['password']:
            print "Correct password"
            print ""
            valid = False
            while valid == False:                 
                choice = raw_input(["Would you like to enter a new password record or retrieve a password? (ENTER/RETRIEVE) Or enter EXIT to quit the program"])
                if choice == "ENTER":
                    # passwordRecordCreate(choice, username)
                    valid = True
                elif choice == "RETRIEVE":
                    # passwordRecordRetrieve(choice, username)
                    valid = True
                elif choice == "EXIT":
                    exit()
                else:
                    print "Invalid choice was entered"
                    valid = False
        else:
            print "Incorrect Password"
            exit()
    else:
        print "Username has not been registered..."
        print ""
        choice = raw_input(["Would you like to create and account? (yes/no)"])
        if choice == "yes":
            create_account(username)
        elif choice == "no":
            exit()
 
def passwordRecordCreate(type, username):
    choice = "yes"
    while choice == "yes":
        yaml_loader(filePath)
        title = raw_input(["Please enter the title of the password you would like to store... (example: facebook, gmail, ect..."])
        password = getpass(["Please enter password for %s..." % title])
        data = {
            "accounts":{
                username:{
                    "titles":{
                        "title": title,
                        "password": password
                    }
                }
            }
        }
        yaml_dump(filePath, data)
        choice = raw_input(["Would you like to enter another password? (yes/no)"])


def passwordRecordRetrieve(type):
    accountTypes = yaml_query(filePath, username)
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
    plainTextPassword = getpass(["Please enter new password..."])
    salt = gensalt()
    hashed = hashpw(plainTextPassword, salt)
    plainTextPasswordCheck = getpass(["Please reenter new password..."])
    hashedCheck = hashpw(plainTextPasswordCheck, salt)
    # match = "no"
    # while match == "no":
    if hashed == hashedCheck:  
        print "Passwords match"
        userPassword = hashed
        # userAccountList.append(newUsername)
        data = {
            "accounts":{
                newUsername:{
                    "password": hashed,
                    "salt": salt
                }
            }
        }
        yaml_loader(filePath)
        yaml_dump(filePath, data)
        match = "yes"
    else:
        print "Passwords do not match"
        match = "no" 
        exit()  

def main():
    account_authenticate()

main()