import os
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    for guild in client.guilds:
        for channel in guild.channels:
            if (type(channel) == discord.TextChannel):
                await channel.send('e')


client.run(TOKEN)
