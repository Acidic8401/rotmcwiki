import discord, datetime, time
from discord.ext import commands

class Core(commands.Cog):
    def __init__(self, client):
        self.client=client

    @commands.command()
    async def ping(self, ctx):
        ping = round(self.client.latency * 1000)
        await ctx.send(f'{ping}ms')

    @commands.command()
    async def uptime(self, ctx):
        current_time = time.time()
        difference = int(round(current_time - self.client.start_time))
        text = str(datetime.timedelta(seconds=difference))
        await ctx.send(text)



def setup(client):
    client.add_cog(Core(client))