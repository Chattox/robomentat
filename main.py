# Robomentat
# Discord bot for data tracking and visualisation
# Written by Chattox

import discord
import keys
import classes
import logging
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


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('On servers:')
    for s in client.servers:
        print('- %s' % s.name)
    print('----------')
    db.startup(client)


@client.event
async def on_message(msg):
    db.usrSendMsg(msg)


client.run(keys.key)
