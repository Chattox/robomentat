# json database to store users, and interactions thereof

import pickle
import keys
import classes as c
import discord
import os

client = discord.Client()

def startup(client):
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
    print("----------")

    # User list update/population
    # First loop through each server the bot is a part of, and pick out the specific server we want
    for s in client.servers:
        if s.id == keys.serverid:
            dbfile = {}
            dblive = {}
            for user in s.members:
                dblive[user.id] = c.User(user.id)
                dblive[user.id].name = user.name
                dblive[user.id].id = user.id
    if os.stat(keys.userdir).st_size == 0:
        print("User log empty, populating...")
        with open(keys.userdir, "wb") as f:
            pickle.dump(dblive, f)
    with open(keys.userdir, "rb") as f:
        dbfile = pickle.load(f)
        for u in dbfile:
            if dbfile[u].name != dblive[u].name:
                dbfile[u].name = dblive[u].name
    with open(keys.userdir, "wb") as f:
        pickle.dump(dbfile, f)
    print("User update complete")
    print("----------")
