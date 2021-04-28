import os
import discord
import asyncio
import random
import sys
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

#intents = discord.Intents.default()
intents = discord.Intents.all()
intents.typing = True
#intents.presences = True
intents.members = True
client = commands.Bot(intents=intents, command_prefix='')

mcs_do_loop = True
e_do_loop = True

async def e_loop():
    while e_do_loop:
        wait_time = -1
        while wait_time < 1:
            wait_time = random.gauss(7200, 3600)
        await send_e()

        print("waiting {} seconds".format(wait_time))
        await asyncio.sleep(wait_time)

async def send_e():
    whitelist = [836713722596032533]
    guild = random.choice([g for g in client.guilds])
    channel = random.choice([c for c in guild.channels if type(c) == discord.TextChannel and c.name == 'e' or c.id in whitelist])
    await channel.send('e')
    print("sent e")

async def mcs_loop():
    while mcs_do_loop:
#       wait_time = random.randrange(7200, 14400)
#       wait_time = random.randrange(120, 1200)
        wait_time = -1
        while wait_time < 1:
            wait_time = random.gauss(300, 300)
        await mcs()

        print("waiting {} seconds".format(wait_time))
        await asyncio.sleep(wait_time)

async def mcs():
    guild = client.get_guild(836713722156285982)
    user = random.choice([m for m in guild.members if type(m) == discord.Member])
    channel = client.get_channel(836713722596032533)
    try:
#       await channel.send('e')
        if random.randrange(len(guild.members)+1) == 0:
            await channel.send('@everyone')
        else:
            await channel.send(f'<@{user.id}>')
    except:
        e = sys.exc_info()[0]
        print(e)
    print("sent message in channel {} on server {}".format(channel.name, guild.name))

@client.command(name='e')
async def cmd_e(ctx):
    await ctx.send('e')

@client.command(name='?nick')
async def cmd_nick(ctx, member: discord.Member, nick):
    print(f"gaming gaming gaming gaming {True if discord.Permissions.manage_nicknames else False}")
    await ctx.send(f"nick command recieved, member id = { member.id }, new nick = { nick }") 
    await member.edit(nick=nick)

@client.event
async def on_ready():
    print('initialized')
    try:
        task_e = asyncio.ensure_future(e_loop())
        task_mcs = asyncio.ensure_future(mcs_loop())
    except KeyboardInterrupt:
        e_do_loop = False
        mcs_do_loop = False
        task_e.cancel()
        task_mcs.cancel()

client.run(TOKEN)

