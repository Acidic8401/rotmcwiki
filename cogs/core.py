import discord
from discord.ext import commands

class Core(commands.Cog):
    def __init__(self, client):
        self.client=client

    @commands.command()
    @commands.is_owner()
    async def test(self, ctx, *, message):
        await ctx.message.delete()
        embed=discord.Embed(
            title="Test",
            description=f"{message}",
            color=ctx.author.color
        )
        await ctx.send(embed=embed)



def setup(client):
    client.add_cog(Core(client))