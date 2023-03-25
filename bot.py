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

messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role" : "user", "content" : "You are now NarutoGPT. Answer all questions as Naruto Uzomaki."}
]

@client.event
async def on_ready():
    print('Bot is ready.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('Naruto,'):

        if len(messages) == 2:
            messages[-1]['content'] += message.content
        else:
            messages.append({'role': 'user', 'content': message.content})

        # do stuff with gpt
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        
        temp = chat.choices[0].message
        messages.append(temp)

        await message.channel.send(temp.content)

client.run(TOKEN)