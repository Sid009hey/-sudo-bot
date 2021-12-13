import discord
import os
import random
from discord.ext import commands

client = discord.Client()

@client.event
async def on_ready():
    print('{0.user} is logged in' .format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$sudo heck'):
        await message.channel.send('`heck succesful` https://cdn.wallpapersafari.com/49/36/4yfL8C.jpg')

    if message.content.startswith('$sudo debug'):
       await message.channel.send('`Debugging... : Debug code:bot_hosted_working`')

    if message.content.startswith('$sudo help'):
        await message.channel.send('https://spark.adobe.com/page/OV74wgwhUK7p9/')

    if message.content.startswith('fuck'):
        await message.channel.send('`STOP SWEARING YOU KNUCKLEHEAD`')

    if message.content.startswith('$sudo heckerman text'):
        await message.channel.send('https://cdn.wallpapersafari.com/49/36/4yfL8C.jpg') 

    if message.content.startswith('$sudo memes'):
        await message.channel.send('https://memes.com/tag/random')  

    if message.content.startswith('$sudo install-package-spec.exe'):
        await message.channel.send('`Installing my owner on to your computer`')

    if message.content.startswith('$sudo virus'):
        await message.channel.send('`Installing the discord-this-is-a-joke-pls-dont-ban-me virus on to vctims computer... Running API... Getting Info... Attack successful !`')

    if message.content.startswith('bello'):
        await message.channel.send('`GO DIE - Eesh 2021`')

    if message.content.startswith('$sudo joke'):
        await message.channel.send(all)

    if message.content.startswith('$sudo emergency'):
        await message.channel.send("`Calling 911 and professional hecker`")

    if message.content.startswith('$sudo can-u-heck-me-a-girlfriend'):
        await message.channel.send("`Go Touch some grass and get a life instead of getting an e-girl in discord`")

    if message.content.startswith('$sudo run virus'):
        await message.channel.send("`running this-is-a-joke-virus.exe on victims IP`")

    if message.content.startswith('$sudo ping'):
        await message.channel.send("`Pinging servers... Pinged Bot servers are connected we have logged in as {0.user}{$sudo Bot#7460}`")

    if message.content.startswith('$sudo hello'):
        await message.channel.send('`print("Hello world")`')
        
    if message.content.startswith('$sudo cringe'):
        await message.channel.send('https://www.youtube.com/watch?v=R3z1X5EeFTQ')
    if message.content.startswith('$sudo rickroll'):
        await message.channel.send('https://c.tenor.com/x8v1oNUOmg4AAAAd/rickroll-roll.gif')

    if message.content.startswith('$sudo drip'):
        await message.channel.send('https://c.tenor.com/T7qNVNvzyUwAAAAM/chips-ahoy-cookie.gif')

    if message.content.startswith('$sudo website'):
        await message.channel.send('https://spark.adobe.com/page/OV74wgwhUK7p9/')

#below code can delete sudo bot 
    if message.content.startswith('$sudo delete sudo'):
        await message.channel.send('`Deleting directories and files destroying physical servers... DELETED ! $sudo will now be offline`')
      
    if message.content.startswith('$sudo matrix'):
        await message.channel.send('secret')
      
client.run(os.getenv('token'))
