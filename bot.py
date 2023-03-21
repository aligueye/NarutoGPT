import os
import discord
import openai
from discord.ext import commands

from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.all()
client = commands.Bot(command_prefix='!', intents=intents)

openai.api_key = os.getenv('OPENAI_API_KEY')

# chat = openai.ChatCompletion.create(
#   model="gpt-3.5-turbo",
#   messages=[
#         {"role": "system", "content": "You are a helpful assistant."},
#         {"role" : "user", "content" : "Who is Naruto Uzomaki?"}
#     ]
# )

# print(chat)

@client.event
async def on_ready():
    print('Bot is ready.')

@client.command()
async def yo(ctx):
    await ctx.send('RASENGAN!!!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('Naruto,'):

        # do stuff with gpt

        await message.channel.send('Woi woi woi')

client.run(TOKEN)