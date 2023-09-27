import discord
import os
import random
# from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')

intents = discord.Intents.default()
intents.message_content = True
bot = discord.Client(command_prefix='!',intents=intents)

general_id = 1153738280622379011

quotes = ['Learning is a daily thing, wisdom an endless pursuit. -Unknown', 
          'If a man knows not to which port he sails, no wind is favorable. -Seneca',
          'If you want to improve, be content to be thought foolish and stupid. -Epictetus',
          'The key is to keep company only with people who uplift you, whose presence calls forth your best. -Epictetus',
          'How long can you afford to put off who you really want to be? Your nobler self cannot wait any longer. Decide to be extraordinary and do what you need to do now. -Epictetus',
          'Just because something is hard to master, do not think it is humanly impossible, but, if a thing is humanly possible, consider it within your reach. -Marcus Aurelius',
          'The reason why we have two ears and only one mouth is so we should listen more and talk less. -Zeno of Citium',
          'We suffer more often in imagination than in reality. -Seneca',
          'Because other people are fools, mus tyou be so too?. -Marcus Aurelius',
          'Bitter are the roots of study, but how sweet is their fruit. -Cato',
          'The world makes way for the man who knows where he is going. -Ralph Waldo Emerson',
          'We must remember, there is no easy way. -Ryan Holiday',
          'Our greatest weakness lies in giving up. The most certain way to succeed is always to try just one more time. -Thomas Edison',
          'Difficulties strengthen the mind as labor does the body. -Seneca'
          ]

@bot.event
async def on_ready():
    channel = bot.get_channel(general_id)
    if channel:
        await channel.send(f'Botistoteles is here,   (⌐■_■)☞')
    

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    if message.content.startswith('!hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('!quote'):
        await message.channel.send(random.choice(quotes))



bot.run(TOKEN)