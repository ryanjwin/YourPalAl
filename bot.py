import os

import random

import discord
# import pycord
from dotenv import load_dotenv
import pyjokes
from jokeapi import Jokes

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
async def on_message(message):
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

    if message.content.lower() == "!pyjoke":
        joke = pyjokes.get_joke()
        await message.channel.send(joke)

    if message.content.lower() == '!chucknorris':
        joke = pyjokes.get_joke(category='chuck')
        await message.channel.send(joke)

    if message.content.lower() == '!pun':
        jokes = await Jokes()
        joke = await jokes.get_joke(blacklist=['nsfw'], category=['pun'])
        await message.channel.send(joke['setup'])
        await message.channel.send(joke['delivery'])

    if message.content.lower() == '!joke':
        jokes = await Jokes()
        joke = await jokes.get_joke(blacklist=['nsfw'], category=['misc'])
        await message.channel.send(joke['setup'])
        await message.channel.send(joke['delivery'])

    if message.content.lower() == '!programming':
        jokes = await Jokes()
        joke = await jokes.get_joke(blacklist=['nsfw'], category=['programming'])
        await message.channel.send(joke['setup'])
        await message.channel.send(joke['delivery'])

    if message.content.lower() == '!dark':
        jokes = await Jokes()
        joke = await jokes.get_joke(category=['dark'])
        await message.channel.send(joke['setup'])
        await message.channel.send(joke['delivery'])


client.run(TOKEN)



