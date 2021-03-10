import os
import asyncio

import discord
from dotenv import load_dotenv

import duckLogger

load_dotenv()
TOKEN = os.getenv('DUCK_TOKEN')

# print(TOKEN)

client = discord.Client()

intents = discord.Intents.all()
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.content == "!ducks":
        # Can't be called from the devotion channel
        if message.channel.name == "gaming":
            return
        send = ""
        users = duckLogger.getInfo()
        for user in users:
            send = send + f'{user.name} has devoted {user.timesDucked} times\n'
        await message.channel.send(send)

    if message.channel.name == "gaming":
        # If bot sends message, doesn't count
        if message.author == client.user:
            return

        users = duckLogger.getInfo()
        # for user in users:
        #     print(user.formatReturn())
        userIndex = duckLogger.inUserList(message.author.name, users)
        print(userIndex)

        if userIndex == "no user with that name":
            print("|||||||")
            user = duckLogger.user(message.author.name, 1)
            users.append(user)
        else:
            print("-------")
            users[userIndex].timesDucked = int(users[userIndex].timesDucked) + 1
            print(users[userIndex].timesDucked)
        duckLogger.writeInfo(users)
        print('hi')
    else:
        print('hello')

    print(message.content)


client.run(TOKEN)