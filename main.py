# Robomentat
# Discord bot for data tracking and visualisation
# Written by Chattox

import discord
import os
import keys
import logging
import pickle

# Set error logging
logger = logging.getLogger('discord')
logger.setLevel(logging.INFO)
handler = logging.FileHandler(filename='./logs/robomentat.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

description = "It is by will alone I set my mind in motion"

client = discord.Client()
userManifest = {}
channelManifest = {}  # These are dicts of the user and channel objects respectively


# User object
class User:
    def __init__(self, userid):
        self.userid = userid

    name = ''
    # Two dictionaries, voice stores channel name : time spent in it,
    # text stores channel name : # of messages sent
    voiceChannels = {}
    textChannels = {}


class Channel:
    def __init__(self, channelid):
        self.channelid = channelid

    name = ''
    # Whether the channel is voice or text
    isVoice = ''
    usage = {}  # Just the one dict here, since time spent and messages sent are essentially the same


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('On servers:')
    for s in client.servers:
        print('- %s' % s.name)
    print('----------')

    # Check log file tree is in place, if not then make it
    logpath = "./logs"
    if not os.path.isdir(logpath):
        print("Log folder not found")
        print("Creating directory")
        os.makedirs(logpath)
        print("Log directory created, creating log files")
        f = open(keys.chanlogdir, "w+")
        f.write("# Channel logs")
        f.close()
        print("- Channels")
        f = open(keys.userlogdir, "w+")
        f.write("# User logs")
        f.close()
        print("- Users")
        print("File creation complete")
        print("----------")

    # Check the log files exist, if not then create
    try:
        chan = open(keys.chanlogdir, "r")
        users = open(keys.userlogdir, "r")
        print("Logs found")
        print("----------")
        chan.close()
        users.close()
    except IOError:
        chan = open(keys.chanlogdir, "w+")
        users = open(keys.userlogdir, "w+")
        pickle.dump("", open(keys.usermanifestdir, "wb+"))
        pickle.dump("", open(keys.chanmanifestdir, "wb+"))
        print("Log files not found\nCreating log files")
        chan.write("")
        chan.close()
        users.write("")
        users.close()
        print("Logs created")
        print("----------")

    # Get list of users
    # First loop through each server the bot is a part of, and pick out the specific server we want

    userPairs = {}
    userPairsFile = {}
    userManifest = {}
    for s in client.servers:
        if s.id == keys.serverid:
            for user in s.members:  # Load up userPairs
                userPairs[user.id] = user.name
            userfile = open(keys.userlogdir, "r")
            for line in userfile:  # Load up userPairsFile
                userid, username = line.split(",")
                username = username.replace("\n", "")
                userPairsFile[userid] = username
            userfile.close()

            # Then compare userPairs and userPairsFile, updating userPairsFile accordingly.
            updated = 0
            for u in userPairs:
                try:
                    if userPairs[u] == userPairsFile[u]:
                        print(userPairs[u], "found:")
                except KeyError:
                    print("New user:", userPairs[u], "adding to database.")
                    userPairsFile[u] = userPairs[u]
                    userManifest[u] = User(u)
                    userManifest[u].name = userPairs[u]
                    updated = 1
                if userPairs[u] == userPairsFile[u]:
                    print(userPairs[u], "up to date.")
                else:
                    print("User mismatch:", userPairs[u], "was", userPairsFile[u] + ". Updating")
                    userPairsFile[u] = userPairs[u]
                    userManifest[u].name = userPairs[u]
                    updated = 1
            # Then write the new updated userPairs to file
            if updated > 0:
                userfile = open(keys.userlogdir, "w")
                for u in userPairs:
                    userfile.write(u+","+userPairsFile[u]+"\n")
                userfile.close()
                with open(keys.usermanifestdir, "wb") as f:
                    pickle.dump(userManifest, f)
                print("User file check complete")
            else:
                print("User file check complete, no updates required.")

            with open(keys.usermanifestdir, "rb") as f:
                userManifest = pickle.load(f)
                for i in userManifest:
                    print(userManifest[i].userid, userManifest[i].name)


client.run(keys.key)
