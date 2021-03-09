import os
import asyncio

import discord
from dotenv import load_dotenv

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
    if message.channel.name == "gaming":
        print('hi')
    else:
        print('hello')

    print(message.content)



client.run(TOKEN)