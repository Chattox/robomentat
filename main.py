# Robomentat
# Discord bot for data tracking and visualisation
# Written by Chattox

import discord
import os
import keys
import logging
import pickle
import database_io as db

# Set error logging
logger = logging.getLogger('discord')
logger.setLevel(logging.INFO)
try:
    f = open("robomentat.log", "x")
    f.close()
except FileExistsError:
    pass
handler = logging.FileHandler(filename='robomentat.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

description = "It is by will alone I set my mind in motion"

client = discord.Client()


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

    db.startup()

    # Get list of users
    # First loop through each server the bot is a part of, and pick out the specific server we want
    for s in client.servers:
        if s.id == keys.serverid:
            userDict = {}
            userDictFile = {}
            # First, generate userDict from discord live
            for user in s.members:
                userDict[user.id] = User(user.id)  # Create new user object with the member ID
                userDict[user.id].name = user.name  # Update user object with their Discord name
                userDict[user.id].id = user.id
            # Then, generate userDictFile from the save file we already have
            with open(keys.userdir, "wb") as f:
                pickle.dump(userDict, f)
            with open(keys.userdir, "rb") as f:
                userDictFile = pickle.load(f)
                print("hodor")
                # for user in userDictFile:
                #     print(userDictFile[user].name)
                #     print(userDictFile[user].userid)
                #     print("---")





    # userPairs = {}
    # userPairsFile = {}
    # userManifest = {}
    # for s in client.servers:
    #     if s.id == keys.serverid:
    #         for user in s.members:  # Load up userPairs
    #             userPairs[user.id] = user.name.encode('utf-8')
    #         userfile = open(keys.userlogdir, "r")
    #         for line in userfile:  # Load up userPairsFile
    #             userid, username = line.split(",")
    #             username = username.replace("\n", "")
    #             userPairsFile[userid] = username
    #         userfile.close()
    #
    #         # Then compare userPairs and userPairsFile, updating userPairsFile accordingly.
    #         updated = 0
    #         for u in userPairs:
    #             try:
    #                 if userPairs[u] == userPairsFile[u]:
    #                     print(userPairs[u], "found:")
    #             except KeyError:
    #                 print("New user:", userPairs[u], "adding to database.")
    #                 userPairsFile[u] = userPairs[u]
    #                 userManifest[u] = User(u)
    #                 userManifest[u].name = userPairs[u]
    #                 updated = 1
    #             if userPairs[u] == userPairsFile[u]:
    #                 print(userPairs[u], "up to date.")
    #             else:
    #                 print("User mismatch:", userPairs[u], "was", userPairsFile[u] + ". Updating")
    #                 userPairsFile[u] = userPairs[u]
    #                 userManifest[u].name = userPairs[u]
    #                 updated = 1
    #         # Then write the new updated userPairs to file
    #         if updated > 0:
    #             userfile = open(keys.userlogdir, "w")
    #             for u in userPairs:
    #                 userfile.write(u+","+userPairsFile[u].decode('utf-8')+"\n")
    #             userfile.close()
    #             with open(keys.usermanifestdir, "wb") as f:
    #                 pickle.dump(userManifest, f)
    #             print("User file check complete")
    #         else:
    #             print("User file check complete, no updates required.")
    #
    #         with open(keys.usermanifestdir, "rb") as f:
    #             userManifest = pickle.load(f)
    #             for i in userManifest:
    #                 print(userManifest[i].userid, userManifest[i].name)


client.run(keys.key)
