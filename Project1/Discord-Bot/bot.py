import os

import discord
import random
from dotenv import load_dotenv

load_dotenv()
#print(os.getenv('DISCORD_TOKEN'))
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]

    hitchhiker_quotes = [
        'There is an art, it says, or rather, a knack to flying. The knack lies in learning how to throw yourself at the ground and miss.',
        'It is a mistake to think you can solve any major problems just with potatoes.',
        'In the beginning the Universe was created. This has made a lot of people very angry and been widely regarded as a bad move.',
        'A common mistake that people make when trying to design something completely foolproof is to underestimate the ingenuity of complete fools.',
    ]

    if message.content == 'towel!':
        #response = random.choice(brooklyn_99_quotes)
        response = random.choice(hitchhiker_quotes)
        await message.channel.send(response)

    #Assortment of 'It's always sunny' quotes
    sunny_quotes = [
        'Can I offer you a nice egg in this trying time?',
        'Oh, look at me! The millionaire who goes to see doctors!',
        'I\'m not fat. I\'m cultivating mass',
        'Oh, you unzipped me! It\'s all coming back! It\'s all coming back; I hate you! It\'s all coming back, you understand?? I DON\'T LIKE IT! I DON\'T LIKE TO THINK ABOUT IT!',
        'Is your cat making TOO MUCH NOISE ALL OF THE TIME?',
        'Well, I don\'t know how many years on this Earth I got left. I\'m gonna get real weird with it',
         ]


    if message.content == 'sunny!':
        response = random.choice(sunny_quotes)
        await message.channel.send(response)
    

client.run(TOKEN)
