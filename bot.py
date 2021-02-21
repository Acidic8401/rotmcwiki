import discord
from discord.ext import commands
from dotenv import load_dotenv
import os 
import json
load_dotenv()
token=os.getenv("TOKEN")

def get_prefix(client, message):
    with open('prefixes.json', 'r') as f:
        prefixes=json.load(f)

    return prefixes[str(message.guild.id)]

client=commands.Bot(command_prefix=get_prefix)
client.remove_command("help")

@client.event
async def on_ready():
    print('Bot is ready')

@client.event
async def on_guild_join(guild):
    with open('prefixes.json', 'r') as f:
        prefixes=json.load(f)

    prefixes[str(guild.id)] = ';'

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

@client.event
async def on_guild_remove(guild):
    with open('prefixes.json', 'r') as f:
        prefixes=json.load(f)
    
    prefixes.pop(str(guild.id))

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

@client.command()
@commands.guild_only()
@commands.has_permissions(administrator=True)
async def prefix(ctx, prefix):
    with open('prefixes.json', 'r') as f:
        prefixes=json.load(f)
    
    prefixes[str(ctx.guild.id)] = prefix

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)
    await ctx.send(f'Prefix has been changed to: `{prefix}`')

@client.command()
@commands.is_owner()
async def quit(ctx):
    await ctx.send("Shutting down the bot")
    await client.logout()

@client.command()
@commands.is_owner()
async def load(ctx, extension):
    if ctx.author.id == 613793967871492131:
        client.load_extension(f'cogs.{extension}')
@client.command()
@commands.is_owner()
async def unload(ctx, extension):
    if ctx.author.id == 613793967871492131:
        client.cdunload_extension(f'cogs.{extension}')
        print(f'{extension} has been unloaded')
@client.command()
@commands.is_owner()
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