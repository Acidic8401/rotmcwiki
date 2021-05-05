import discord 
def char(ctx, weapon, armour, type, atk, spd, bhp, health, eva, vit, defence, crithit, critdam, tn):
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
        value=f"`Attack:` {atk} \n `Defence:` {defence} \n `Speed:` {spd} \n `Evasion:` {eva} \n `Vitality:` {vit} \n `Health:` {health} \n `Base HP:` {bhp} \n `Crit Hit:` {crithit} \n `Crit Damage:` {critdam}",
        inline=False
    )
    embed.set_thumbnail(url=tn)
    return embed
def dungs(ctx, gear, abilities, gems, whites, tn, pots, runes, droplocs, colour, treq):
    embed=discord.Embed(
        title="**Dungeon info**",
        color=ctx.author.color
    )
    if runes:
        embed.add_field(
            name="**Drops**",
            value=f"`Gear:` {gear} \n `Abilities:` {abilities} \n `Gems:` {gems} \n `Whites:` {whites}\n `Pots:` {pots} \n `Drop Locations:` {droplocs} \n `Tier Points:` {treq} \n `Other:` Runes"
        )
    else:
        embed.add_field(
            name="**Drops**",
            value=f"`Gear:` {gear} \n `Abilities:` {abilities} \n `Gems:` {gems} \n `Whites:` {whites}\n `Drop Locations:` {droplocs} \n `Pots:` {pots} \n `Tier Points:` {treq}"
        )

    embed.color=int(colour)
    embed.set_thumbnail(url=tn)
    embed.set_footer(text="For more information do ;info <itemname>")
    return embed
def armours(ctx, slot, classes, displayname, levelreq, dropsfrom, stats, gems, runes, essence, tn, exalted, colour):
    if slot in ["Head", "Chest", "Leggings", "Feet"]:
        if essence == "True" and exalted == "True":
            embed=discord.Embed(
                title="**Item info**",
                description=f"`Level Requirement:` {levelreq} \n `Slot:` {slot} \n `Classes:` {classes} \n `Display Name:` {displayname} \n `Exalted:` True \n `Stats:` {stats} \n `Gem Sockets:` {gems} \n `Rune Sockets:` {runes} \n `Essence Sockets:` 1",
                color=int(colour)
            )
        elif essence == "False" and exalted == "True":
            embed=discord.Embed(
                title="**Item info**",
                description=f"`Level Requirement:` {levelreq} \n `Slot:` {slot} \n `Classes:` {classes} \n `Display Name:` {displayname} \n `Exalted:` True \n `Stats:` {stats} \n `Gem Sockets:` {gems} \n `Rune Sockets:` {runes}",
                color=int(colour)
            )   
        elif essence == "True" and exalted == "False":
            embed=discord.Embed(
                title="**Item info**",
                description=f"`Level Requirement:` {levelreq} \n `Slot:` {slot} \n `Classes:` {classes} \n `Display Name:` {displayname} \n `Stats:` {stats} \n `Gem Sockets:` {gems} \n `Rune Sockets:` {runes} \n `Essence Sockets:` 1",
                color=int(colour)
            )
        elif essence == "False" and exalted== "False":
            embed=discord.Embed(
                title="**Item info**",
                description=f"`Level Requirement:` {levelreq} \n `Slot:` {slot} \n `Classes:` {classes} \n `Display Name:` {displayname} \n `Drop Location:` {dropsfrom} \n `Stats:` {stats} \n `Gem Sockets:` {gems} \n `Rune Sockets:` {runes}",
                color=int(colour)
            )
    embed.set_thumbnail(url=tn)
    return embed
def weapons(ctx, dname, lreq, droploc, exalted, dmg, rge, shots, velocity, pierces, cd, tpe, classes, gem, tn, colour):
    if exalted == "True":
        embed=discord.Embed(
            title="**Weapon info**",
            description=f"`Display Name:` {dname} \n `Level Requirement:` {lreq} \n `Exalted:` {exalted} \n `Damage:` {dmg} \n `Range:` {rge} \n `Shots:` {shots} \n `Velocity:` {velocity} \n `Pierces:` {pierces} \n `Cooldown:` {cd} \n `Type:` {tpe} \n `Classes:` {classes} \n `Gem Sockets:` {gem}",
            color=ctx.author.color
            )
    else:
        embed=discord.Embed(
            title="**Weapon info**",
            description=f"`Display Name:` {dname} \n `Level Requirement:` {lreq} \n `Drop Location:` {droploc} \n `Damage:` {dmg} \n `Range:` {rge} \n `Shots:` {shots} \n `Velocity:` {velocity} \n `Pierces:` {pierces} \n `Cooldown:` {cd} \n `Type:` {tpe} \n `Classes:` {classes} \n `Gem Sockets:` {gem}",
            color=ctx.author.color
            )
    embed.set_thumbnail(url=tn)
    embed.color=int(colour)
    return embed
def abilities(dname, lreq, droploc, exalted, cd, ability, gem, tn, colour):
    if exalted == "True":
        embed=discord.Embed(
            title="**Ability info**",
            description=f"`Display Name:` {dname} \n `Level Requirement:` {lreq} \n `Exalted:` True \n `Cooldown:` {cd} \n `Ability:` {ability} \n `Gem Slots:` {gem}"
        )
    else:
        embed=discord.Embed(
            title="**Ability info**",
            description=f"`Display Name:` {dname} \n `Level Requirement:` {lreq} \n `Drop Location:` {droploc} \n `Cooldown:` {cd} \n `Ability:` {ability} \n `Gem Slots:` {gem}"
        )

    embed.set_thumbnail(url=tn)
    embed.color=int(colour)
    return embed
def tarmours(tpe, gem, lreq, stats, classes, tier, name, colour, tn):
    if tier in ["9", "10", "11"]:
        embed=discord.Embed(
            title="**Armour info**",
            description=f"`Armour Type:` {tpe} \n `Set Name:` {name} \n `Tier:` {tier} \n `Level Requirement:` {lreq} \n `Gem Sockets:` {gem} \n `Rune Sockets:` 1 \n `Classes:` {classes} \n `Stats:` {stats}"
        )
    elif tier in ["4", "3", "2", "1"]:
        embed=discord.Embed(
            title="**Armour info**",
            description=f"`Armour Type:` {tpe} \n `Set Name:` {name} \n `Tier:` {tier} \n `Level Requirement:` {lreq} \n `Classes:` {classes} \n `Stats:` {stats}"
        )
    else:
        embed=discord.Embed(
            title="**Armour info**",
            description=f"`Armour Type:` {tpe} \n `Set Name:` {name} \n `Tier:` {tier} \n `Level Requirement:` {lreq} \n `Gem Sockets:` {gem} \n `Classes:` {classes} \n `Stats:` {stats}"
        )
    embed.set_thumbnail(url=tn)
    embed.color=int(colour)
    return embed
def tweapons(tpe, damage, rge, shots, velocity, pierces, cd, lreq, classes, name, gem, tier, colour, tn):
    if tier in ["1", "2", "3", "4"]:
        embed=discord.Embed(
            title="**Weapon info**",
            description=f"`Weapon Type:` {tpe} \n `Classes:` {classes} \n `Tier:` {tier} \n `Display Name:` {name} \n `Damage:` {damage} \n `Range:` {rge} \n `Shots:` {shots} \n `Velocity:` {velocity} \n `Pierces:` {pierces} \n `Cooldown:` {cd}"
        )
    else:
        embed=discord.Embed(
            title="**Weapon info**",
            description=f"`Weapon Type:` {tpe} \n `Classes:` {classes} \n `Tier:` {tier} \n `Gem Sockets:` {gem} \n `Display Name:` {name} \n `Damage:` {damage} \n `Range:` {rge} \n `Shots:` {shots} \n `Velocity:` {velocity} \n `Pierces:` {pierces} \n `Cooldown:` {cd}"
        )
    embed.set_thumbnail(url=tn)
    embed.color=int(colour)
    return embed
def elytras(defense, attack, speed, dodge, health, gem, name, colour, tn):
    embed=discord.Embed(
        title="**Elytra info**",
        description=f"`Display Name:` {name} \n `Defense Bonus:` {defense} \n `Attack Bonus:` {attack} \n `Speed Bonus:` {speed} \n `Dodge Bonus:` {dodge} \n `Health Bonus:` {health} \n `Gem Sockets:` {gem} \n `Rune Sockets:` 1 \n `Essence Sockets:` 1"
    )
    embed.set_thumbnail(url=tn)
    embed.color=int(colour)
    return embed
def dust():
    embed=discord.Embed(
        title="**Dust info**",
        description = "Dust is used to make the success rate of gems. There are 5 different kinds of dust."
    )