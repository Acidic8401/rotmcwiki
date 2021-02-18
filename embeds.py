import discord 
def char(ctx, weapon, armour, type, atk, spd, bhp, health, eva, vit, defence, tn):
    embed=discord.Embed(
        title="**Class info**",
        color=ctx.author.color
    )
    embed.add_field(
        name="**General info**",
        value=f"`Weapon:` {weapon} \n `Armour type:` {armour} \n `Class category:` {type}",
        inline=False
    )
    embed.add_field(
        name="**Stat info**",
        value=f"`Attack:` {atk} \n `Defence:` {defence} \n `Speed:` {spd} \n `Evasion:` {eva} \n `Vitality:` {vit} \n `Health:` {health} \n `Base HP:` {bhp}",
        inline=False
    )
    embed.set_thumbnail(url=tn)
    return embed
def dungs(ctx, gear, abilities, gems, whites, tn, white_url, pots):
    embed=discord.Embed(
        title="**Dungeon info**",
        color=ctx.author.color
    )
    embed.add_field(
        name="**Drops**",
        value=f"`Gear:` {gear} \n `Abilities:` {abilities} \n `Gems:` {gems} \n `Whites:` {whites}\n `Pots:` {pots}"
    )
    embed.set_thumbnail(url=tn)
    embed.set_footer(icon_url=white_url, text="For more information do !info <itemname>")
    return embed