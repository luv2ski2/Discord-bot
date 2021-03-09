# bot.py

# This isn't my main bot
# This is a different one for aping james, it failed

import os
import asyncio

import discord
from dotenv import load_dotenv


# load_dotenv()
# TOKEN = os.getenv('DISCORD_TOKEN')
# print(TOKEN)

# This isn't the correct token
# This will fail if you try to run it
TOKEN = "ODA2NjkwMTc2NjYyNTAzNDQ1.YBtGxQ.3UdneWzSpFK9j7EkFBSmqqs3tEI"
client = discord.Client()

intents = discord.Intents.all()
client = discord.Client(intents=intents)

apeCount = 0
# server = 9
game = client.guilds
def findServer(name):
    for server in client.guilds:
        if server.name == name:
            #print(server.name)
            return server
    return "No server"

def findMember(name, server):
    #print(server.name)
    #print(server.members)
    for member in server.members:
        #print(member.name)
        if member.name == name:
            #print(member.name)
            return member
    return "No member"


@client.event
async def on_ready():
    # gaming = 0
    print(f'{client.user} has connected to Discord!')


@client.event
async  def on_message(message):
    if message.content.startswith("Ape James"):
        james = findMember("Tigersol", findServer("Test Server"))
        for i in range(60):
            await message.channel.send(james.mention + " stinky ape man change my name back")

    if "hello there" in message.content.lower():
        await message.channel.send("General Kenobi")
        await asyncio.sleep(1)
        await message.channel.send("You are a bold one!")
    if "story time" in message.content.lower():
        if message.author.name != "Luv2ski2":
            await message.channel.send("Stinky")
        else:
            await message.channel.send("Did you ever hear the tragedy of Darth Plagueis The Wise? I thought not. It\'s not a story the Jedi would tell you. It\'s a Sith legend. Darth Plagueis was a Dark Lord of the Sith, so powerful and so wise he could use the Force to influence the midichlorians to create life… He had such a knowledge of the dark side that he could even keep the ones he cared about from dying. The dark side of the Force is a pathway to many abilities some consider to be unnatural. He became so powerful… the only thing he was afraid of was losing his power, which eventually, of course, he did. Unfortunately, he taught his apprentice everything he knew, then his apprentice killed him in his sleep. Ironic. He could save others from death, but not himself.")
    if message.guild:
        if message.author == client.user:
            return
        if message.content == "Joker is hype":
            await message.channel.send("Correct")

        #await message.author.send("hi")
    if not message.guild:
        if message.author.name == "Luv2ski2":
            await message.channel.send("Hi " + message.author.name)

        if message.content == "Ape Ian":
            ian = findMember("Mr_Jankman", findServer("Test Server"))
            for i in range(40):
                await ian.send("stinky")
        if message.content == "Ape Korben":
            k = findMember("Ka-boom360", findServer("Test Server"))
            for i in range(40):
                await k.send("stinky")
        if message.content == "Ape James":
            james = findMember("Tigersol", findServer("Test Server"))
            for i in range(1):
                global apeCount
                await james.send("stinky")
                print(apeCount)
                apeCount += 1
        if message.content == "Ape Adam":
            adam = findMember("G0ld3n", findServer("D&D 2"))
            print(adam.name)
            for i in range(400):
                await adam.send("stinky")
                print(apeCount)
                apeCount += 1
            print("Done")
        # if message.content == "Ape Vermin":
        #     #global apeCount
        #     vermin = findMember("vermin", findServer("D&D 2"))
        #     print(vermin.name + " " + str(apeCount))
        #     apeCount += 1
        #     for i in range(400):
        #         await vermin.send("stinky")
client.run(TOKEN)
