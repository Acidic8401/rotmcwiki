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
        self.tcave=["tcave", "cave"]
        self.kraken=["krak", "kraken"]
        self.fung=["fungal", "fc", "fungc", "fung"]
        self.cult=["cult", "cultist"]
        self.golem=["golem", "void"]
        self.shatts=["shatters", "shatts"]
        #items
        self.crown=["the forgotten crown", "crown"]
        self.thood=["thood", "twih"]
        self.svisor=["svisor", "visor"]
        self.vhat=["vhat", "voidh", "vh"]
        self.sarmour=["sarmour", "speccloth", "sarmor"]
        self.cgreaves=["greaves", "cgreaves"]
        self.crobe=["crobe", "rcronus"]
        self.lboots=["lboots"]
        self.ssandals=["spookys", "spooky", "ssandals", "sandals"]
        print('Wiki intisialised')

    @commands.command(aliases=["wiki"])
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
        elif terms in self.abyss:
            terms="abyss"
        elif terms in self.udl:
            terms="udl"
        elif terms in self.davy:
            terms="davy"
        elif terms in self.kraken:
            terms="kraken"
        elif terms in self.fung:
            terms="fung"
        elif terms in self.cult:
            terms="cult"
        elif terms in self.golem:
            terms="golem"
        elif terms in self.shatts:
            terms="shatters"
        elif terms in self.crown:
            terms="crown"
        elif terms in self.thood:
            terms="thood"
        elif terms in self.svisor:
            terms="svisor"
        elif terms in self.vhat:
            terms="vhat"
        elif terms in self.sarmour:
            terms="sarmour"
        elif terms in self.cgreaves:
            terms="cgreaves"
        elif terms in self.tcave:
            terms="tcave"
        elif terms in self.crobe:
            terms="crobe"
        elif terms in self.lboots:
            terms="lboots"
        elif terms in self.ssandals:
            terms="ssandals"
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
        elif terms in ["abyss", "udl", "davy", "tcave", "kraken", "fung", "cult", "golem", "shatters"]:
            with open(r'C:\Users\Bailey\Documents\Programs\rotmc\rotmcwiki\rotmc.json') as f:
                f = json.load(f)
            data=f["dungs"][terms]
            tn=data["tn"]
            drops=data["drops"]            
            gear=drops["gear"]
            gems=drops["gems"]
            pots=drops["pots"]
            pots=', '.join(pots)
            if drops["runes"] == "True":
                runes=True
            else:
                runes=False
            abilities=drops["abilities"]
            whites=drops["whites"]
            whites=', '.join(whites)
            print('getting embed')
            droploc=data["droploc"]
            droploc=', '.join(droploc)
            em=embeds.dungs(ctx, gear, abilities, gems, whites, tn, pots, runes, droploc)
            await ctx.send(embed=em)
        elif terms in ["crown", "thood", "svisor", "vhat", "sarmour", "cgreaves", "crobe", "lboots", "ssandals"]:
            with open(r'C:\Users\Bailey\Documents\Programs\rotmc\rotmcwiki\rotmc.json') as f:
                f = json.load(f)
            data=f["items"][terms]
            slot = data["slot"]
            classes=data["classes"]
            classes=', '.join(classes)
            displayname=data["displayname"]
            levelreq=data["levelreq"]
            dropsfrom=data["dropsfrom"]
            stats=data["stats"]
            stats=', '.join(stats)
            gems=data["gem"]
            runes=data["runes"]
            essence=data["essence"]
            tn=data["tn"]
            em=embeds.items(ctx, slot, classes, displayname, levelreq, dropsfrom, stats, gems, runes, essence, tn)
            await ctx.send(embed=em)

        

def setup(client):
    client.add_cog(Wiki(client))