import discord 
from discord.ext import commands
import json
import embeds

class Wiki(commands.Cog):
    def __init__(self, client):
        self.client=client
        #Classes
        self.warr=["warr", "warrior", "war"]
        self.knight=["knight"]
        self.necro=["necro", "necromancer", "nec"]
        self.battlemage=["mage", "battle", "bm", "battlemage"]
        self.huntress=["hunt", "hunty", "huntress"]
        self.sin=["sin", "asin", "assassin", "ass"]
        self.rogue=["rogue"]
        self.ninja=["ninja"]
        self.samurai=["sam", "samurai", "samu"]
        #Dungs
        self.abyss=["abby", "abyss", "aod", "abyssofdemons", "aby"]
        self.udl=["lair", "udl"]
        self.davy=["davy", "davies", "davyjones'locker"]
        self.tcave=["tcave", "cave"]
        self.kraken=["krak", "kraken"]
        self.fung=["fungal", "fc", "fungc", "fung"]
        self.cult=["cult", "cultist"]
        self.golem=["golem", "void"]
        self.shatts=["shatters", "shatts"]
        #UT Armours
        self.crown=["theforgottencrown", "crown"]
        self.thood=["thood", "twih"]
        self.svisor=["svisor", "visor"]
        self.vhat=["vhat", "voidh", "vh"]
        self.sarmour=["sarmour", "speccloth", "sarmor"]
        self.cgreaves=["crayfishgreaves", "cgreaves"]
        self.crobe=["crobe", "rcronus"]
        self.lboots=["lboots"]
        self.ssandals=["spookys", "spooky", "ssandals", "sandals"]
        self.smask=["smask"] 
        self.chood=["chood", "cult hood"]
        self.bplate=["bplate", "breastplate"]
        self.flegs=["flegs", "forst leggings", "fleggings"]
        self.fboots=["fboots", "fboot", "fungalboots"]
        self.llegs=["llegs", "lchaps", "lightningchaps"]
        self.oboots=["oboots", "onyxboots"]
        self.ochest=["ochest", "onyxchest"]
        self.ochaps=["ochaps", "onyxchaps"]
        #T11 Armours
        self.mmask=["mmask", "moonmask"]
        self.mchest=["mchest", "moonchest"]
        self.mgreaves=["mgreaves", "mlegs", "moonlegs"]
        self.mboots=["mboots"]
        self.ehat=["ehat"]
        self.earmour=["earmour", "earmor", "echest"]
        self.echaps=["echaps", "elegs"]
        self.esandals=["eboots", "esandals"]
        self.cehood=["cehood", "celhood", "celestialhood"]
        self.cerobe=["cerobe", "celrobe", "celestialrobe"]
        self.celegs=["celegs", "cellegs", "celestiallegs"]
        self.ceboots=["ceboots", "celboots", "celestialboots"]
        #Exalted Armours
        self.ebplate=["exaltedbplate", "ebplate"]
        self.ellegs=["exllegs", "ellegs", "elchaps"]
        self.echood=["echood", "exchood", "exaltedchood"]
        self.esmask=["esmask", "exsmask", "exaltedsmask"]
        self.essandals=["essandals", "exssandals", "exaltedssandals"]
        self.elboots=["elboots", "exlboots", "exaltedlboots"]
        self.ecrobe=["ecrobe", "excrobe", "exaltedcrobe"]
        self.eflegs=["eflegs", "exflegs", "exaltedflegs"]
        self.efboots=["efboots", "exfboots", "exaltedfboots"]
        self.eoboots=["eoboots", "eonyxboots", "exoboots", "exaltedoboots"]
        self.eochest=["eochest", "eonyxchest", "exochest", "exaltedochest"]
        self.eochaps=["eochaps", "eonyxchaps", "exochaps", "exaltedochaps"]
        self.ecgreaves=["ecgreaves"]
        self.esarmour=["esarmour", "exsamour", "esarmor", "exsarmor", "escloth"]
        self.evhat=["evhat", "exvhat", "evoidhat"]
        self.esvisor=["esvisor", "exsvisor", "evisor"]
        self.ethood=["ethood", "exthood", "etwilight"]
        self.ecrown=["ecrown", "excrown", "exaltedcrown"]
        #UT Katanas
        self.dkat=["dkat", "doomkat", "dkatana", "doomkatana"]
        self.edkat=["edkat", "edoomkat", "edkatana", "edoomkatana"]
        self.kendo=["kendostick", "kstick", "kendo"]
        self.ekendo=["ekendostick", "ekstick", "ekendo"]
        self.okat=["okat", "okatana", "onyxkat", "onyxkatana"]
        self.eokat=["eokat", "eokatana", "eonyxkat", "eonyxkatana"]
        #UT Bows
        self.dbow=["dbow", "doombow", "db"]
        self.edbow=["edbow", "edoombow", "edb", "exdbow"]
        self.cbow=["cbow", "coralbow"]
        self.ecbow=["ecbow", "excbow", "ecoralbow", "excoralbow"]
        self.lbow=["lbow", "lightningbows", "lightbow"]
        self.elbow=["elbow", "exlbow", "exlightningbow", "elightningbow", "elightbow", "exlightbow"]
        self.bbow=["bbow", "blunderbow"]
        self.ebbow=["ebbow", "eblunderbow", "exbbow", "exblunderbow"]
        self.obow=["obow", "onyxbow", "olbow", "onyxlongbow"]
        self.eobow=["eobow", "exobow", "eonyxbow", "exonyxbow", "eolbow", "exolbow", "eonyxlongbow", "exonyxlongbow"]
        #UT Daggers 
        self.sdagger=["sdagger", "spiritdagger", "sdag"]
        self.esdagger=["esdagger", "esdag", "espiritdagger"]
        self.cdirk=["cdirk"]
        self.ecdirk=["ecdirk", "excdirk"]
        self.ddagger=["ddagger", "demonicdagger", "demdagger"]
        self.eddagger=["eddagger", "exddagger"]
        self.gdagger=["gdagger", "grassdagger", "cgdagger", "crossdagger"]
        self.egdagger=["egdagger", "egrassdagger", "ecgdagger", "ecrossdagger"]
        self.odagger=["odagger", "ocutter", "onyxdagger", "onyxcutter"]
        self.eodagger=["eodagger", "eocutter", "eonyxdagger", "eonyxcutter"]
        #UT Staves
        self.shovel=["gshovel", "gravediggers", "shovel", "gravediggersshovel"]
        self.eshovel=["egshovel", "egravediggers", "eshovel", "egravediggersshovel"]
        self.cultstaff=["cultstaff", "cstaff", "sacstaff", "unholystaff"]
        self.ecultstaff=["ecultstaff", "ecstaff", "esacstaff", "eunholystaff"]
        self.crystalstaff=["crystalstaff", "crystaff", "crstaff"]
        self.ecrystalstaff=["ecrystalstaff", "ecrystaff", "ecrstaff"]
        self.asteroid=["asteroid", "asteroidstaff", "asterstaff"]
        self.easteroid=["easteroid", "easteroidstaff", "easterstaff"]
        self.ostaff=["ostaff", "oscythe", "onyxstaff", "onyxscythe"]
        self.eostaff=["eostaff", "eoscythe", "eonyxstaff", "eonyxscythe"]
        #UT Swords
        self.cutlass=["cutlass", "cut"]
        self.ecutlass=["ecutlass", "ecut"]
        self.dblade=["dblade", "demonblade", "demonicblade"]
        self.edblade=["edblade", "edemonblade", "edemonicblade"]
        self.gsword=["gsword", "asword", "guardiansword", "ancientsword"]
        self.egsword=["egsword", "easword", "eguardiansword", "eancientsword"]
        self.tcleaver=["tcleaver", "cleaver", "titaniumcleaver"]
        self.etcleaver=["etcleaver", "ecleaver", "etitaniumcleaver"]
        self.osword=["osword", "onyxsword", "ogreatsword", "onyxgreatsword"]
        self.eosword=["eosword", "eonyxsword", "eogreatsword", "eonyxgreatsword"]
        #Orbs
        self.ot1=["ot1", "orbt1", "t1orb", "t1o"]
        self.ot2=["ot2", "orbt2", "t2orb", "t2o"]
        self.ot3=["ot3", "orbt3", "t3orb", "t3o"]
        self.ot4=["ot4", "orbt4", "t4orb", "t4o"]
        self.ot5=["ot5", "orbt5", "t5orb", "t5o"]
        self.conflict=["conflict", "orbofconflict"]
        self.econflict=["econflict", "eorbofconflict"]
        self.sorb=["sloworb", "sorb", "storb", "slowtouchorb"]
        self.esorb=["esloworb", "esorb", "estorb", "eslowtouchorb"]
        #Cloaks
        self.ct1=["ct1", "cloakt1", "t1c", "t1cloak"]
        self.ct2=["ct2", "cloakt2", "t2c", "t2cloak"]
        self.ct3=["ct3", "cloakt3", "t3c", "t3cloak"]
        self.ct4=["ct4", "cloakt4", "t4c", "t4cloak"]
        self.ct5=["ct5", "cloakt5", "t5c", "t5cloak"]
        self.bcloak=["bcloak", "bloodycloak"]
        self.ebcloak=["ebcloak", "ebloodycloak"]
        self.ccloak=["ccloak", "combustioncloak"]
        self.eccloak=["eccloak", "ecombustioncloak"]
        #Helmets
        self.ht1=["ht1", "helmett1", "t1h", "t1helmet"]
        self.ht2=["ht2", "helmett2", "t2h", "t2helmet"]
        self.ht3=["ht3", "helmett3", "t3h", "t3helmet"]
        self.ht4=["ht4", "helmett4", "t4h", "t4helmet"]
        self.ht5=["ht5", "helmett5", "t5h", "t5helmet"]
        self.jugg=["jug", "jugg"]
        self.ejugg=["ejug", "ejugg"]
        self.ehelm=["ehelm", "ehelmet"]
        self.eehelm=["eehelm", "eehelmet"]
        #Poisons
        self.pt1=["pt1", "poisont1", "t1p", "t1poison"]
        self.pt2=["pt2", "poisont2", "t2p", "t2poison"]
        self.pt3=["pt3", "poisont3", "t3p", "t3poison"]
        self.pt4=["pt4", "poisont4", "t4p", "t4poison"]
        self.pt5=["pt5", "poisont5", "t5p", "t5poison"]
        self.ppoison=["ppoison", "plaguepoison"]
        self.eppoison=["eppoison", "eplaguepoison"]
        self.cfang=["cfang", "fpoison", "fangpoison", "crystallisedfang"]
        self.ecfang=["ecfang", "efpoison", "efangpoison", "ecrystallisedfang"]
        print('Wiki intisialised')

    @commands.command(aliases=["wiki"])
    async def info(self, ctx, *, terms):
        terms=terms.lower()
        terms = terms.replace(" ", "")
        #Classes
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
        elif terms in self.ninja:
            terms = "ninja"
        elif terms in self.samurai:
            terms = "samurai"
        #Dungeons
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
        #Armours
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
        elif terms in self.smask:
            terms="smask"
        elif terms in self.bplate:
            terms="bplate"
        elif terms in self.chood:
            terms="chood"
        elif terms in self.flegs:
            terms="flegs"
        elif terms in self.fboots:
            terms="fboots"
        elif terms in self.llegs:
            terms = "llegs"
        elif terms in self.oboots:
            terms = "oboots"
        elif terms in self.ochest:
            terms = "ochest"
        elif terms in self.ochaps:
            terms = "ochaps"
        #T11s
        elif terms in self.mmask:
            terms = "mmask"
        elif terms in self.mchest:
            terms = "mchest"
        elif terms in self.mgreaves:
            terms = "mgreaves"
        elif terms in self.mboots:
            terms = "mboots"
        elif terms in self.ehat:
            terms = "ehat"
        elif terms in self.earmour:
            terms = "earmour"
        elif terms in self.echaps:
            terms = "echaps"
        elif terms in self.esandals:
            terms = "eboots"
        elif terms in self.cehood:
            terms="cehood"
        elif terms in self.cerobe:
            terms="cerobe"
        elif terms in self.celegs:
            terms ="celegs"
        elif terms in self.ceboots:
            terms = "ceboots"
        #Exalted Armours
        elif terms in self.ebplate:
            terms="ebplate"
        elif terms in self.ellegs:
            terms = "ellegs"
        elif terms in self.echood:
            terms = "echood"
        elif terms in self.esmask:
            terms = "esmask"
        elif terms in self.essandals:
            terms = "essandals"
        elif terms in self.elboots:
            terms = "elboots"
        elif terms in self.ecrobe:
            terms = "ecrobe"
        elif terms in self.eflegs:
            terms = "eflegs"
        elif terms in self.efboots:
            terms = "efboots"
        elif terms in self.eoboots:
            terms = "eoboots"
        elif terms in self.eochest:
            terms = "eochest"
        elif terms in self.eochaps:
            terms = "eochaps"
        elif terms in self.ecgreaves:
            terms = "ecgreaves"
        elif terms in self.esarmour:
            terms = "esarmour"
        elif terms in self.evhat:
            terms = "evhat"
        elif terms in self.esvisor:
            terms = "esvisor"
        elif terms in self.ethood:
            terms = "ethood"
        elif terms in self.ecrown:
            terms = "ecrown"
        #UT Katanas
        elif terms in self.dkat:
            terms = "dkat"
        elif terms in self.edkat:
            terms = "edkat"
        elif terms in self.kendo:
            terms = "kendo"
        elif terms in self.ekendo:
            terms = "ekendo"
        elif terms in self.okat:
            terms = "okat"
        elif terms in self.eokat:
            terms = "eokat"
        #UT Bows
        elif terms in self.dbow:
            terms = "dbow"
        elif terms in self.edbow:
            terms = "edbow"
        elif terms in self.cbow:
            terms = "cbow"
        elif terms in self.ecbow:
            terms = "ecbow"
        elif terms in self.lbow:
            terms = "lbow"
        elif terms in self.elbow:
            terms = "elbow"
        elif terms in self.bbow:
            terms = "bbow"
        elif terms in self.ebbow:
            terms = "ebbow"
        elif terms in self.obow:
            terms = "obow"
        elif terms in self.eobow:
            terms = "eobow"
        #UT Daggers
        elif terms in self.sdagger:
            terms = "sdagger"
        elif terms in self.esdagger:
            terms = "esdagger"
        elif terms in self.cdirk:
            terms = "cdirk"
        elif terms in self.ecdirk:
            terms = "ecdirk"
        elif terms in self.ddagger:
            terms = "ddagger"
        elif terms in self.eddagger:
            terms = "eddagger"
        elif terms in self.gdagger:
            terms = "gdagger"
        elif terms in self.egdagger:
            terms = "egdagger"
        elif terms in self.odagger:
            terms = "odagger"
        elif terms in self.eodagger:
            terms = "eodagger"
        #UT Staves
        elif terms in self.shovel:
            terms = "shovel"
        elif terms in self.eshovel:
            terms = "eshovel"
        elif terms in self.cultstaff:
            terms = "cultstaff"
        elif terms in self.ecultstaff:
            terms = "ecultstaff"
        elif terms in self.crystalstaff:
            terms = "crystalstaff"
        elif terms in self.ecrystalstaff:
            terms = "ecrystalstaff"
        elif terms in self.asteroid:
            terms = "asteroid"
        elif terms in self.easteroid:
            terms="easteroid"
        elif terms in self.ostaff:
            terms = "ostaff"
        elif terms in self.eostaff:
            terms = "eostaff"
        #UT Swords
        elif terms in self.cutlass:
            terms = "cutlass"
        elif terms in self.ecutlass:
            terms = "ecutlass"
        elif terms in self.dblade:
            terms = "dblade"
        elif terms in self.edblade:
            terms = "edblade"
        elif terms in self.gsword:
            terms = "gsword"
        elif terms in self.egsword:
            terms = "egsword"
        elif terms in self.tcleaver:
            terms = "tcleaver"
        elif terms in self.etcleaver:
            terms = "etcleaver"
        elif terms in self.osword:
            terms = "osword"
        elif terms in self.eosword:
            terms = "eosword"
        #Orbs
        elif terms in self.ot1:
            terms = "ot1"
        elif terms in self.ot2:
            terms = "ot2"
        elif terms in self.ot3:
            terms = "ot3"
        elif terms in self.ot4:
            terms = "ot4"
        elif terms in self.ot5:
            terms = "ot5"
        elif terms in self.conflict:
            terms = "conflict"
        elif terms in self.econflict:
            terms = "econflict"
        elif terms in self.sorb:
            terms = "sorb"
        elif terms in self.esorb:
            terms = "esorb"
        #Cloaks
        elif terms in self.ct1:
            terms = "ct1"
        elif terms in self.ct2:
            terms = "ct2"
        elif terms in self.ct3:
            terms = "ct3"
        elif terms in self.ct4:
            terms = "ct4"
        elif terms in self.ct5:
            terms = "ct5"
        elif terms in self.bcloak:
            terms="bcloak"
        elif terms in self.ebcloak:
            terms="ebcloak"
        elif terms in self.ccloak:
            terms="ccloak"
        elif terms in self.eccloak:
            terms = "eccloak"
        #Helmets
        elif terms in self.ht1:
            terms="ht1"
        elif terms in self.ht2:
            terms="ht2"
        elif terms in self.ht3:
            terms="ht3"
        elif terms in self.ht4:
            terms="ht4"
        elif terms in self.ht5:
            terms="ht5"
        elif terms in self.jugg:
            terms="jugg"
        elif terms in self.ejugg:
            terms="ejugg"
        elif terms in self.ehelm:
            terms="ehelm"
        elif terms in self.eehelm:
            terms = "eehelm"
        #Poisons
        elif terms in self.pt1:
            terms="pt1"
        elif terms in self.pt2:
            terms="pt2"
        elif terms in self.pt3:
            terms="pt3"
        elif terms in self.pt4:
            terms="pt4"
        elif terms in self.pt5:
            terms="pt5"
        elif terms in self.ppoison:
            terms="ppoison"
        elif terms in self.eppoison:
            terms="eppoison"
        elif terms in self.cfang:
            terms="cfang"
        elif terms in self.ecfang:
            terms="ecfang"
        if terms in ["warrior", "knight", "necro", "battlemage", "huntress", "assassin", "rogue", "ninja", "samurai"]:
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
            crithit=stats["crithit"]
            critdam=stats["critdam"]
            tn=data["tn"]
            em=embeds.char(ctx, weapon, armour, type, atk, spd, bhp, health, eva, vit, defence, crithit, critdam, tn)
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
        elif terms in ["eochest", "eochaps", "ochest", "ochaps", "oboots","eoboots","eflegs", "fboots", "efboots", "ecrobe", "crown", "thood", "svisor", "vhat", "sarmour", "cgreaves", "crobe", "lboots", "ssandals", "smask", "chood", "bplate", "flegs", "mmask", "mchest", "mgreaves", "mboots", "ehat", "earmour", "echaps", "eboots", "cehood", "cerobe", "celegs", "ceboots", "ebplate", "llegs", "ellegs", "echood", "esmask", "essandals", "elboots", "ecgreaves", "esarmour", "evhat", "esvisor", "ethood", "ecrown"]:
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
            exalted=data["exalted"]
            tn=data["tn"]
            colour=data["colour"]
            em=embeds.armours(ctx, slot, classes, displayname, levelreq, dropsfrom, stats, gems, runes, essence, tn, exalted, colour)
            await ctx.send(embed=em)
        elif terms in ["dbow", "edbow", "dkat", "edkat", "kendo", "ekendo", "okat", "eokat", "cbow", "ecbow", "lbow", "elbow", "bbow", "ebbow", "obow", "eobow", "sdagger", "esdagger", "cdirk", "ecdirk", "ddagger", "eddagger", "gdagger", "egdagger", "odagger", "eodagger", "shovel", "eshovel", "cultstaff", "ecultstaff", "crystalstaff", "ecrystalstaff", "asteroid", "easteroid", "ostaff", "eostaff", "cutlass", "ecutlass", "dblade", "edblade", "gsword", "egsword", "tcleaver", "etcleaver", "osword", "eosword"]:
            with open(r'C:\Users\Bailey\Documents\Programs\rotmc\rotmcwiki\rotmc.json') as f:
                f = json.load(f)
            data=f["items"][terms]
            dname=data["displayname"]
            lreq=data["levelreq"]
            droploc=data["dropsfrom"]
            exalted=data["exalted"]
            dmg=data["damage"]
            rge=data["range"]
            shots=data["shots"]
            velocity=data["velocity"]
            pierces=data["pierces"]
            cd=data["cd"]
            tpe=data["type"]
            classes=data["classes"]
            classes=', '.join(classes)
            gem=data["gem"]
            tn=data["tn"]
            colour=data["colour"]
            em=embeds.weapons(ctx, dname, lreq, droploc, exalted, dmg, rge, shots, velocity, pierces, cd, tpe, classes, gem, tn, colour)
            await ctx.send(embed=em)
        elif terms in ["ot1", "ot2", "ot3", "ot4", "ot5", "conflict", "econflict", "sorb", "esorb", "ct1", "ct2", "ct3", "ct4", "ct5", "bcloak", "ebcloak", "ccloak", "eccloak", "ht1", "ht2", "ht3", "ht4", "ht5", "jugg", "ejugg", "ehelm", "eehelm", "pt1", "pt2", "pt3", "pt4", "pt5", "ppoison", "eppoison", "cfang", "ecfang"]:
            with open(r'C:\Users\Bailey\Documents\Programs\rotmc\rotmcwiki\rotmc.json') as f:
                f = json.load(f)
                data=f["items"][terms]
                dname=data["displayname"]
                lreq = data["levelreq"]
                droploc = data["droploc"]
                exalted = data["exalted"]
                cd=data["cd"]
                ability=data["ability"]
                gem=data["gem"]
                colour=data["colour"]
                tn=data["tn"]
                em=embeds.abilities(dname, lreq, droploc, exalted, cd, ability, gem, tn, colour)
                await ctx.send(embed=em)
        else:
            await ctx.send(f"couldn't find {terms} in the database, please try again")

        

def setup(client):
    client.add_cog(Wiki(client))