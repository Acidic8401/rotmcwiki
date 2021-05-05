import discord
from discord.ext import commands
import datetime


class Admin(commands.Cog):
    def __init__(self, client):
        self.client=client
    
    @commands.command()
    async def uptime(self, ctx):
        uptime_secs = round((datetime.datetime.utcnow() - self.client.start_time).total_seconds())
        print(str(datetime.timedelta(seconds=uptime_seconds)))
        await ctx.send(f"Current Uptime: {'{:0>8}'.format(str(datetime.timedelta(seconds=uptime_seconds)))}")

def setup(client):
    client.add_cog(Admin(client))