import discord
import json
import asyncio
from discord.ext import commands
import re

botconfig = json.load(open('config.json', 'r'))

bot = commands.Bot(command_prefix='...', self_bot=True, case_insensitive=True)

def filterMessage(msg: discord.Message):
    if not msg.channel.id in botconfig['channels']:
        return False
    if msg.author.id != botconfig['treatBot']:
        return False
    if len(msg.embeds) == 0:
        return False
    return True

@bot.event
async def on_ready():
    print('Logged in as {}!'.format(bot.user))

@bot.event
async def on_message(message: discord.Message):
    if not filterMessage(message): return
    
    embed: discord.Embed = message.embeds[0]

    if 'h!trick' in embed.description:
        await message.channel.send('h!trick')
        print('Attempted snipe with h!trick...')
    elif 'h!treat' in embed.description:
        await message.channel.send('h!treat')
        print('Attempted snipe with h!treat...')
    else:
        print('Ignoring embed titled "{}"'.format(embed.title))

@bot.event
async def on_message_edit(before: discord.Message, after: discord.Message):
    if not filterMessage(before): return

    if before.embeds[0].description == after.embeds[0].description:
        return
    
    embed: discord.Embed = after.embeds[0]

    if not 'Happy Halloween' in embed.title:
        print('Ignoring embed titled "{}"...'.format(embed.title))
        return

    item = re.search('\\*\\*(.*)\\*\\*', embed.description).groups()[0]

    if str(bot.user.id) in embed.description:
        print('Successfully sniped {}!'.format(item))
        async with before.channel.typing():
            await asyncio.sleep(5)
        await before.channel.send('LOL get sniped')
    else:
        print('{} was sniped by someone else :('.format(item))
        async with before.channel.typing():
            await asyncio.sleep(5)
        await before.channel.send('wtf how were you faster than me')

bot.run(botconfig['token'], bot=False)
