import discord
from discord.ext import commands

class Core(commands.Cog):
    def __init__(self, client):
        self.client=client

    @commands.command()
    async def ping(self, ctx):
        ping = round(self.client.latency * 1000)
        await ctx.send(f'{ping}ms')



def setup(client):
    client.add_cog(Core(client))