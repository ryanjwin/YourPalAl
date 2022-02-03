import os

import random

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    m1 = message
    if message.author == client.user:
        return
    # knock knock joke
    if message.content.lower() == "knock knock":
        await message.channel.send("Who's there?")
        msg = await client.wait_for('message', check=lambda message: message.author == m1.author)
        reply = msg.content + " who?"
        await message.channel.send(reply)
        msg = await client.wait_for('message', check=lambda message: message.author == m1.author)
        await message.channel.send("jajajaja")

    # what a save
    if message.content.lower() == "what a save":
        for i in range(3):
            await message.channel.send("What a save!")
        await message.channel.send("Chat disabled for 3 seconds")
    
    # roast me
    possibleRoasts = ["What did the 2 say to the 10?\n roast me hahaha", "I'd slap you, \nbut that would be animal abuse.", "I am not saying that I hate you,\n I'm just saying if you got hit by a bus, I would be driving that bus.", "https://www.menshealth.com/uk/style/a29772406/receding-hairline/", "When I see your face, there is not a thing I would change...\n except the direction I'm walking in", "A little advice homie\nhttps://www.wikihow.com/Flirt"]
    if message.content.lower() == "roast me":
        idx = random.randint(0, len(possibleRoasts) - 1)
        await message.channel.send(possibleRoasts[idx])

client.run(TOKEN)



