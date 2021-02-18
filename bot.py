import discord
from discord.ext import commands
from dotenv import load_dotenv
import os 
load_dotenv()
token=os.getenv("TOKEN")

client=commands.Bot(command_prefix= '!')
client.remove_command("help")

@client.event
async def on_ready():
    print('Bot is ready')

@client.command()
async def load(ctx, extension):
    if ctx.author.id == 613793967871492131:
        client.load_extension(f'cogs.{extension}')
@client.command()
async def unload(ctx, extension):
    if ctx.author.id == 613793967871492131:
        client.cdunload_extension(f'cogs.{extension}')
        print(f'{extension} has been unloaded')
@client.command()
async def rload(ctx, extension):
    if ctx.author.id == 613793967871492131:
        client.unload_extension(f'cogs.{extension}')
        print(f'{extension} has been unloaded')
        client.load_extension(f'cogs.{extension}')
        print(f'{extension} has been reloaded')

for filename in os.listdir(r'C:\Users\Bailey\Documents\Programs\rotmc\rotmcwiki\cogs'):
    if filename.endswith('py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(token)