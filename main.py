# Robomentat
# Discord bot for data tracking and visualisation
# Written by Chattox

import discord
import os
import keys

description = "It is by will alone I set my mind in motion"

client = discord.Client()


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('On servers:')
    for s in client.servers:
        print('- %s' % s.name)
    print('----------')
    logpath = "./logs"
    if not os.path.isdir(logpath):
        print("Log folder not found")
        print("Creating directory")
        os.makedirs(logpath)
        print("Log directory created, creating log files")
        f = open("./logs/channels.log","w+")
        f.write("# Channel logs")
        f.close()
        print("- Channels")
        f = open("./logs/users.log","w+")
        f.write("# User logs")
        f.close()
        print("- Users")
        print("File creation complete")
        print("----------")
        print("Robomentat ready to serve")

    try:
        chan = open("./logs/channels.log","r")
        users = open("./logs/users.log","r")
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




client.run(keys.key)
