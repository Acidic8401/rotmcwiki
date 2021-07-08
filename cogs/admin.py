import discord
from discord.ext import commands
import dislash
import datetime
import embeds

class Admin(commands.Cog):
    def __init__(self, client):
        self.client=client

    @commands.command()
    async def help(self, ctx):
        msg = await ctx.send(embed=embeds.help(ctx),
                            components=[
                                dislash.SelectMenu(
                                   custom_id="test",
                                   placeholder="What do you need help with?",
                                   max_values=1,
                                   options=[
                                      dislash.SelectOption(label="Dungeons", value="dungs"),
                                      dislash.SelectOption(label="Gems", value="gems"),
                                      dislash.SelectOption(label="Weapons", value="weapons"),
                                      dislash.SelectOption(label="Armours", value="armours"),
                                      dislash.SelectOption(label="Abilities", value="abilities"),
                                      dislash.SelectOption(label="Elytras", value="elytras"),
                                      dislash.SelectOption(label="Dust", value="dust")
                                   ]
                                )])

        def check(inter):
            # inter is instance of MessageInteraction
            # read more about it in "Objects and methods" section
            return inter.author == ctx.author

        # Wait for a menu click under the message you've just sent
        inter = await msg.wait_for_dropdown(check)
        # Tell which options you received
        values = [option.value for option in inter.select_menu.selected_options]
        await ctx.message.delete()
        if "dungs" in values:
            await msg.edit(embed=embeds.dungeon(ctx), components=None)
        elif "gems" in values:
            await msg.edit(embed=embeds.gems_help(ctx), components=None)
        elif "weapons" in values:
            await msg.edit(embed=embeds.weapons_help(ctx), components=None)
        elif "armours" in values:
            await msg.edit(embed=embeds.armour_help(ctx), components=None)
        elif "abilities" in values:
            await msg.edit(embed=embeds.abilities_help(ctx), components=None)
        elif "elytras" in values:
            await msg.edit(embed=embeds.elytrainfo(ctx), components=None)
        elif "dust" in values:
            await msg.edit(embed=embeds.dust(ctx), components=None)
        else:
            await msg.edit(content="Not yet implemented", components=None, embed=None)
        


def setup(client):
    client.add_cog(Admin(client))