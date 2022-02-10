import os

import random

import discord
from dotenv import load_dotenv

# create list of possibleRoasts from local text file
# name text file roast.txt
with open('roast.txt') as roast:
    possibleRoasts = roast.readlines()

# load bot token from env file
# token can be created by creating an application on discord here: https://discord.com/login?redirect_to=%2Fdevelopers%2Fapplications

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')


client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!') # prints in console if bot connection was successful

@client.event
async def on_message(message, possibleRoasts):
    user_typing = message.author
    if message.author == client.user:
        return # ensures that message is not from the bot
    # knock knock joke
    if message.content.lower() == "knock knock":
        await message.channel.send("Who's there?")
        msg = await client.wait_for('message', check=lambda message: message.author == user_typing) # make sure that second message is the same author
        reply = msg.content + " who?"
        await message.channel.send(reply)
        msg = await client.wait_for('message', check=lambda message: message.author == user_typing) # make sure that second message is the same author
        await message.channel.send("jajajaja")

    # what a save (rocket league reference)
    if message.content.lower() == "what a save":
        for i in range(3):
            await message.channel.send("What a save!")
        await message.channel.send("Chat disabled for 3 seconds")
    
    # roast me
    if message.content.lower() == "roast me":
        idx = random.randint(0, len(possibleRoasts) - 1) # generates random integer for index in list
        await message.channel.send(possibleRoasts[idx])

client.run(TOKEN)



