import os
import discord
import asyncio
import random
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

do_loop = True
async def timer_loop():
	while do_loop:
            await send_e()
            wait_time = random.randrange(7200, 14400)
            print("waiting {} seconds".format(wait_time))
            await asyncio.sleep(wait_time)

async def send_e():
    for guild in client.guilds:
        channel = None
        while (type(channel) != discord.TextChannel):
            channel = guild.channels[random.randrange(0, len(guild.channels))]
        await channel.send('e')
        print("sent e in channel {} on server {}".format(channel.name, guild.name))

@client.event
async def on_ready():
	try:
		task = asyncio.ensure_future(timer_loop())
	except KeyboardInterrupt:
		do_loop = False
		task.cancel()

client.run(TOKEN)

