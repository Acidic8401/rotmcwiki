import discord 
from discord.ext import commands
import json
import embeds

class Wiki(commands.Cog):
    def __init__(self, client):
        self.client=client
        #classes
        self.warr=["warr", "warrior", "war"]
        self.knight=["knight"]
        self.necro=["necro", "necromancer", "nec"]
        self.battlemage=["mage", "battle", "bm", "battlemage"]
        self.huntress=["hunt", "hunty", "huntress"]
        self.sin=["sin", "asin", "assassin", "ass"]
        self.rogue=["rogue"]
        #dungs
        self.abyss=["abby", "abyss", "aod", "abyss of demons", "aby"]
        self.udl=["lair", "udl"]
        self.davy=["davy", "davies", "davy jones' locker"]
        print('Wiki intisialised')

    @commands.command()
    async def info(self, ctx, *, terms):
        terms=terms.lower()
        if terms in self.warr:
            terms = "warrior"
        elif terms in self.knight:
            terms="knight"
        elif terms in self.necro:
            terms="necro"
        elif terms in self.battlemage:
            terms="battlemage"
        elif terms in self.huntress:
            terms="huntress"
        elif terms in self.sin:
            terms="assassin"
        elif terms in self.rogue:
            terms="rogue"
        if terms in ["warrior", "knight", "necro", "battlemage", "huntress", "assassin", "rogue"]:
            with open(r'C:\Users\Bailey\Documents\Programs\rotmc\rotmcwiki\rotmc.json') as f:
                f = json.load(f)
            data = f["classes"][terms]
            weapon=data["weapon"]
            armour=data["armour"]
            type=data["type"]
            stats=f["classes"][terms]["stats"]
            atk=stats["atk"]
            spd=stats["spd"]
            bhp=stats["bhp"]
            health=stats["health"]
            eva=stats["eva"]
            vit=stats["vit"]
            defence=stats["defence"]
            tn=data["tn"]
            em=embeds.char(ctx, weapon, armour, type, atk, spd, bhp, health, eva, vit, defence, tn)
            await ctx.send(embed=em)
        if terms in self.abyss:
            terms="abyss"
        elif terms in self.udl:
            terms="udl"
        elif terms in self.davy:
            terms="davy"
        if terms in ["abyss", "udl", "davy"]:
            with open(r'C:\Users\Bailey\Documents\Programs\rotmc\rotmcwiki\rotmc.json') as f:
                f = json.load(f)
            data=f["dungs"][terms]
            tn=data["tn"]
            drops=data["drops"]            
            gear=drops["gear"]
            gems=drops["gems"]
            pots=drops["pots"]
            pots=pots[0]
            abilities=drops["abilities"]
            whites=drops["whites"]
            white_url=data["whiteurl"]
            whites=', '.join(whites)
            em=embeds.dungs(ctx, gear, abilities, gems, whites, tn, white_url, pots)
            await ctx.send(embed=em)
        

def setup(client):
    client.add_cog(Wiki(client))