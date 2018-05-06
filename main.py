# Robomentat
# Discord bot for data tracking and visualisation
# Written by Chattox

import discord
import os
import keys
import logging

# Set error logging
logger = logging.getLogger('discord')
logger.setLevel(logging.WARNING)
handler = logging.FileHandler(filename='./logs/robomentat.log', encoding='utf-8', mode='w')
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
    usage = {} # Just the one dict here, since time spent and messages sent are essentially the same

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
    except IOError:
        chan = open(keys.chanlogdir, "w+")
        users = open(keys.userlogdir, "w+")
        print("Log files not found\nCreating log files")
        chan.write("# Channel logs")
        chan.close()
        users.write("# User logs")
        users.close()
        print("Logs created")
        print("----------")

    # Get list of users
    # First loop through each server the bot is a part of, and pick out the specific server we want
    for s in client.servers:
        if s.id == keys.serverid:
            for user in s.members: # Then run through each member on the server and add it to a list.
                userlog = open(keys.userlogdir, "r")
                contents = userlog.read()
                if user.id in contents:
                    print("User", user.name, "already present")
                    userlog.close()
                else:
                    userlog.close()
                    userlog = open(keys.userlogdir, "a")
                    userlog.write(user.name+","+user.id+"\n")
                    print(user.name, "is new, writing to file")
                    userlog.close()



client.run(keys.key)
