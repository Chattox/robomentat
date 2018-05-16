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
        for u in dblive:
            if u not in dbfile:
                print("New user:", dblive[u].name)
                dbfile[u] = dblive[u]
            if dbfile[u].name != dblive[u].name:
                print("Updating", dbfile[c].name, "to", dblive[u].name)
                dbfile[u].name = dblive[u].name
    with open(keys.userdir, "wb") as f:
        pickle.dump(dbfile, f)
    print("User update complete")

    # Channel list update/population
    # Same as before, just for channels
    for s in client.servers:
        if s.id == keys.serverid:
            dblive = {}
            for chan in s.channels:
                dblive[chan.id] = c.Channel(chan.id)
                dblive[chan.id].name = chan.name
                dblive[chan.id].id = chan.id
                dblive[chan.id].isVoice = chan.type == discord.ChannelType.voice
    if os.stat(keys.chandir).st_size == 0:
        print("Channel log empty, populating...")
        with open(keys.chandir, "wb") as f:
            pickle.dump(dblive, f)
    with open(keys.chandir, "rb") as f:
        dbfile = pickle.load(f)
        for ch in dblive:
            if ch not in dbfile:
                print("New channel:", dblive[ch].name)
                dbfile[ch] = dblive[ch]
            if dbfile[ch].name != dblive[ch].name:
                print("Updating", dbfile[ch].name, "to", dblive[ch].name)
                dbfile[ch].name = dblive[ch].name
    with open(keys.chandir, "wb") as f:
        pickle.dump(dbfile, f)
    print("Channel update complete")
    print("----------")

    # Populate/update channel dicts within User objects
    with open(keys.userdir, "rb") as u:
        userFile = pickle.load(u)
    with open(keys.chandir, "rb") as ch:
        chanFile = pickle.load(ch)
    for u in userFile:
        with open(keys.userdir, "rb") as usr:
            userFileTemp = pickle.load(usr)
        print("-", userFileTemp[u].name)
        print("-", userFileTemp[u].voiceChannels)
        for ch in chanFile:
            if chanFile[ch].isVoice == True:
                if ch not in userFile[u].voiceChannels:
                    print("-- Adding voice channel", chanFile[ch].name, "to", userFileTemp[u].name)
                    userFileTemp[u].voiceChannels[ch] = 0
            else:
                if ch not in userFileTemp[u].textChannels:
                    print("-- Adding text channel", chanFile[ch].name, "to", userFileTemp[u].name)
                    userFileTemp[u].textChannels[ch] = 0
        with open(keys.userdir, "wb") as usr:
            pickle.dump(userFileTemp, usr)
    #
    # with open(keys.userdir, "rb") as u:
    #     userRead = pickle.load(u)
    #     for user in userRead:
    #         print(userRead[user].name)
    #         print("-", userRead[user].voiceChannels)


def usrSendMsg(message):
    print(message.author, "sent a message")
    with open(keys.userdir, "rb") as f:
        msgFile = pickle.load(f)
        oldMsgCount = msgFile[message.author.id].textChannels[message.channel.id]
        print("Number of messages so far:", oldMsgCount)
        oldMsgCount += 1
        print("New message count:", oldMsgCount)
        msgFile[message.author.id].textChannels[message.channel.id] = oldMsgCount
    with open(keys.userdir, "wb") as f:
        pickle.dump(msgFile, f)
