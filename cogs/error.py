import discord
from discord.ext import commands

class ErrorHandler(commands.Cog):
  def __init__(self, client):
    self.client=client

  @commands.Cog.listener()
  async def on_command_error(self, ctx: discord.ext.commands.Context, error):
    if hasattr(ctx.command, "on_error"):
      return
    if isinstance(error, commands.CommandNotFound):
      await ctx.message.delete()
      return await ctx.send(content="That command does not exist. If this is an error please DM DevAcidic#9633", delete_after=10)
    if isinstance(error, commands.MissingRequiredArgument):
      embed = discord.Embed(title="Error!", description="You appear to be missing a required argument! \n If this is an error please DM DevAcidic#9633", color=discord.Color.red())
      embed.add_field(name="Missing argument", value=f'`{error.args[0]}`', inline=False)
      return await ctx.send(embed=embed, delete_after=20)

def setup(client):
  client.add_cog(ErrorHandler(client))