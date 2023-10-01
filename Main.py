import discord
import os
import random
import json

from dotenv import load_dotenv

with open('database.json') as database_file:
    database = database_file.read()

data = json.loads(database)

load_dotenv()
TOKEN = os.getenv('TOKEN')

intents = discord.Intents.default()
intents.message_content = True
bot = discord.Client(command_prefix='!',intents=intents)

general_id = 1153738280622379011

@bot.event
async def on_ready():
    channel = bot.get_channel(general_id)
    if channel:
        await channel.send(f'(⌐■_■)☞ \nBotistoteles is here')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    if message.content.startswith('!hello'):
        random_index = random.randint(0, len(data["greetings"])-1)
        await message.channel.send(f'{data["greetings"][random_index]["hello"]} {data["greetings"][random_index]["greeting"]}')
    
    if message.content.startswith('!im good'):
        random_index = random.randint(0, len(data["positive"]) -1)
        await message.channel.send(f'{data["positive"][random_index]["good"]}')

    if message.content.startswith('!not good'):
        random_index = random.randint(0, len(data["negative"]) -1)
        await message.channel.send(f'{data["negative"][random_index]["bad"]}')

    if message.content.startswith('!quote'):
        random_index = random.randint(0, len(data["quotes"])-1)
        await message.channel.send(f'{data["quotes"][random_index]["quote"]}\n-{data["quotes"][random_index]["name"]}')

bot.run(TOKEN)