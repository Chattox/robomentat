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
        f = open("./logs/channels.log", "w+")
        f.write("# Channel logs")
        f.close()
        print("- Channels")
        f = open("./logs/users.log", "w+")
        f.write("# User logs")
        f.close()
        print("- Users")
        print("File creation complete")
        print("----------")
        print("Robomentat ready to serve")

    try:
        chan = open("./logs/channels.log", "r")
        users = open("./logs/users.log", "r")
        print("Logs found")
        print("----------")
        print("Robomentat ready to serve")
    except IOError:
        chan = open("./logs/channels.log", "w+")
        users = open("./logs/users.log", "w+")
        print("Log files not found\nCreating log files")
        chan.write("# Channel logs")
        chan.close()
        users.write("# User logs")
        users.close()
        print("Logs created")
        print("----------")
        print("Robomentat ready to serve")

    # Get


client.run(keys.key)
