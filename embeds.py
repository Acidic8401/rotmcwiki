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
def dungs(ctx, gear, abilities, gems, whites, tn, pots, runes, droplocs):
    embed=discord.Embed(
        title="**Dungeon info**",
        color=ctx.author.color
    )
    if runes:
        embed.add_field(
            name="**Drops**",
            value=f"`Gear:` {gear} \n `Abilities:` {abilities} \n `Gems:` {gems} \n `Whites:` {whites}\n `Pots:` {pots} \n `Drop Locations:` {droplocs} \n `Pots:` {pots} \n`Other:` Runes"
        )
    else:
        embed.add_field(
            name="**Drops**",
            value=f"`Gear:` {gear} \n `Abilities:` {abilities} \n `Gems:` {gems} \n `Whites:` {whites}\n `Drop Locations:` {droplocs} \n `Pots:` {pots}"
        )
    embed.set_thumbnail(url=tn)
    embed.set_footer(text="For more information do ;info <itemname>")
    return embed
def items(ctx, slot, classes, displayname, levelreq, dropsfrom, stats, gems, runes, essence, tn):
    if essence == "True":
        embed=discord.Embed(
            title="**Item info**",
            description=f"`Level Requirement:` {levelreq} \n ccccccc`Slot:` {slot} \n `Classes:` {classes} \n `Display Name:` {displayname} \n `Drop Location:` {dropsfrom} \n `Stats:` {stats} \n `Gem Sockets:` {gems} \n `Rune Sockets:` {runes} \n `Essence Sockets:` 1",
            color=ctx.author.color
        )
    else:
        embed=discord.Embed(
            title="**Item info**",
            description=f"`Level Requirement:` {levelreq} \n `Slot:` {slot} \n `Classes:` {classes} \n `Display Name:` {displayname} \n `Drop Location:` {dropsfrom} \n `Stats:` {stats} \n `Gem Sockets:` {gems} \n `Rune Sockets:` {runes}",
            color=ctx.author.color
        )        
    embed.set_thumbnail(url=tn)
    return embed