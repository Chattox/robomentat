# json database to store users, and interactions thereof

import json
import keys
import discord
import os

def startup():
    logpath = "./logs"
    if not os.path.isdir(logpath):
        print("Log folder not found")
        print("Creating directory")
        os.makedirs(logpath)
        print("Log directory created, creating log files")
        try:
            with open(keys.chandir, "x") as f:
                print("Channel log created")
        except FileExistsError:
            print("Channel log already exists")
        print("- Channels")
        try:
            with open(keys.chandir, "x") as f:
                print("User log created")
        except FileExistsError:
            print("User log already exists")
        print("- Users")
        print("File creation complete")
        print("----------")

    # Check the log files exist, if not then create
    try:
        with open(keys.chandir, "x") as f:
            print("Channel log created")
    except FileExistsError:
        print("Channel log found")
    try:
        with open(keys.userdir, "x") as f:
            print("User log created")
    except FileExistsError:
        print("User log found")