import discord 
from discord.ext import commands
import json
import embeds
import re
from pygicord import Paginator

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
        self.udl=["lair", "udl", "undeadlair"]
        self.davy=["davy", "davies", "davyjoneslocker"]
        self.tcave=["tcave", "cave", "caveofathousandtreasures"]
        self.kraken=["krak", "kraken", "krakensfortress"]
        self.fung=["fungal", "fc", "fungc", "fung", "fungalcavern"]
        self.cult=["cult", "cultist", "cultisthideout"]
        self.golem=["golem", "void", "voidgolem"]
        self.shatts=["shatters", "shatts", "theshatters"]
        #UT Armours
        self.crown=["theforgottencrown", "crown"]
        self.thood=["thood", "twih", "twilighthood"]
        self.svisor=["svisor", "visor", "sentinelsvisors"]
        self.vhat=["vhat", "voidh", "vh", "voidhat"]
        self.sarmour=["sarmour", "speccloth", "sarmor", "spectralclotharmour"]
        self.cgreaves=["crayfishgreaves", "cgreaves"]
        self.crobe=["crobe", "rchronos", "robeofchronos"]
        self.lboots=["lboots", "lightningboots"]
        self.ssandals=["spookys", "spooky", "ssandals", "sandals", "spookysandals"]
        self.smask=["smask", "maskofshaitan", "shaitanmask"] 
        self.chood=["chood", "culthood", "hoodofthecultist"]
        self.bplate=["bplate", "breastplate", "breastplateofnewlife"]
        self.flegs=["flegs", "frostleggings", "fleggings"]
        self.fboots=["fboots", "fboot", "fungalboots"]
        self.llegs=["llegs", "lchaps", "lightningchaps"]
        self.oboots=["oboots", "onyxboots", "onyxsboots"]
        self.ochest=["ochest", "onyxchest", "onyxschestplate"]
        self.ochaps=["ochaps", "onyxchaps", "onyxschaps"]
        #Tiered Heavy Armours
        self.ht11=["heavyt11", "ht11", "t11h", "t11heavy"]
        self.ht10=["heavyt10", "ht10", "t10h", "t10heavy"]
        self.ht9=["heavyt9", "ht9", "t9h", "t9heavy"]
        self.ht8=["heavyt8", "ht8", "t8h", "t8heavy"]
        self.ht7=["heavyt7", "ht7", "t7h", "t7heavy"]
        self.ht6=["heavyt6", "ht6", "t6h", "t6heavy"]
        self.ht5=["heavyt5", "ht5", "t5h", "t5heavy"]
        self.ht4=["heavyt4", "ht4", "t4h", "t4heavy"]
        self.ht3=["heavyt3", "ht3", "t3h", "t3heavy"]
        self.ht2=["heavyt2", "ht2", "t2h", "t2heavy"]
        self.ht1=["heavyt1", "ht1", "t1h", "t1heavy"]
        #Tiered Leather Armours
        self.lt11=["leathert11", "lt11", "t11l", "t11leather"]
        self.lt10=["leathert10", "lt10", "t10l", "t10leather"]
        self.lt9=["leathert9", "lt9", "t9l", "t9leather"]
        self.lt8=["leathert8", "lt8", "t8l", "t8leather"]
        self.lt7=["leathert7", "lt7", "t7l", "t7leather"]
        self.lt6=["leathert6", "lt6", "t6l", "t6leather"]
        self.lt5=["leathert5", "lt5", "t5l", "t5leather"]
        self.lt4=["leathert4", "lt4", "t4l", "t4leather"]
        self.lt3=["leathert3", "lt3", "t3l", "t3leather"]
        self.lt2=["leathert2", "lt2", "t2l", "t2leather"]
        self.lt1=["leathert1", "lt1", "t1l", "t1leather"]
        #Tiered Robe Armours
        self.rt11=["robet11", "rt11", "t11r", "t11robe"]
        self.rt10=["robet10", "rt10", "t10r", "t10robe"]
        self.rt9=["robet9", "rt9", "t9r", "t9robe"]
        self.rt8=["robet8", "rt8", "t8r", "t8robe"]
        self.rt7=["robet7", "rt7", "t7r", "t7robe"]
        self.rt6=["robet6", "rt6", "t6r", "t6robe"]
        self.rt5=["robet5", "rt5", "t5r", "t5robe"]
        self.rt4=["robet4", "rt4", "t4r", "t4robe"]
        self.rt3=["robet3", "rt3", "t3r", "t3robe"]
        self.rt2=["robet2", "rt2", "t2r", "t2robe"]
        self.rt1=["robet1", "rt1", "t1r", "t1robe"]
        #Tiered Katanas
        self.katt1=["katanat1", "t1katana", "t1kat", "katt1"]
        self.katt2=["katanat2", "t2katana", "t2kat", "katt2"]
        self.katt3=["katanat3", "t3katana", "t3kat", "katt3"]
        self.katt4=["katanat4", "t4katana", "t4kat", "katt4"]
        self.katt5=["katanat5", "t5katana", "t5kat", "katt5"]
        self.katt6=["katanat6", "t6katana", "t6kat", "katt6"]
        self.katt7=["katanat7", "t7katana", "t7kat", "katt7"]
        self.katt8=["katanat8", "t8katana", "t8kat", "katt8"]
        self.katt9=["katanat9", "t9katana", "t9kat", "katt9"]
        self.katt10=["katanat10", "t10katana", "t10kat", "katt10"]
        self.katt11=["katanat11", "t11katana", "t11kat", "katt11"]
        #Tiered Bows
        self.bowt1=["bowt1", "t1bow", "t1b", "bt1"]
        self.bowt2=["bowt2", "t2bow", "t2b", "bt2"]
        self.bowt3=["bowt3", "t3bow", "t3b", "bt3"]
        self.bowt4=["bowt4", "t4bow", "t4b", "bt4"]
        self.bowt5=["bowt5", "t5bow", "t5b", "bt5"]
        self.bowt6=["bowt6", "t6bow", "t6b", "bt6"]
        self.bowt7=["bowt7", "t7bow", "t7b", "bt7"]
        self.bowt8=["bowt8", "t8bow", "t8b", "bt8"]
        self.bowt9=["bowt9", "t9bow", "t9b", "bt9"]
        self.bowt10=["bowt10", "t10bow", "t10b", "bt10"]
        self.bowt11=["bowt11", "t11bow", "t11b", "bt11"]
        #Tiered Daggers
        self.daggert1=["daggert1", "t1dagger", "t1dag", "dagt1"]
        self.daggert2=["daggert1", "t2dagger", "t2dag", "dagt2"]
        self.daggert3=["daggert3", "t3dagger", "t3dag", "dagt3"]
        self.daggert4=["daggert4", "t4dagger", "t4dag", "dagt4"]
        self.daggert5=["daggert5", "t5dagger", "t5dag", "dagt5"]
        self.daggert6=["daggert6", "t6dagger", "t6dag", "dagt6"]
        self.daggert7=["daggert7", "t7dagger", "t7dag", "dagt7"]
        self.daggert8=["daggert8", "t8dagger", "t8dag", "dagt8"]
        self.daggert9=["daggert9", "t9dagger", "t9dag", "dagt9"]
        self.daggert10=["daggert10", "t10dagger", "t10dag", "dagt10"]
        self.daggert11=["daggert11", "t11dagger", "t11dag", "dagt11"]
        #Tiered Staves
        self.stafft1=["stafft1", "t1staff", "t1sta", "stat1"]
        self.stafft2=["stafft2", "t2staff", "t2sta", "stat2"]
        self.stafft3=["stafft3", "t3staff", "t3sta", "stat3"]
        self.stafft4=["stafft4", "t4staff", "t4sta", "stat4"]
        self.stafft5=["stafft5", "t5staff", "t5sta", "stat5"]
        self.stafft6=["stafft6", "t6staff", "t6sta", "stat6"]
        self.stafft7=["stafft7", "t7staff", "t7sta", "stat7"]
        self.stafft8=["stafft8", "t8staff", "t8sta", "stat8"]
        self.stafft9=["stafft9", "t9staff", "t9sta", "stat9"]
        self.stafft10=["stafft10", "t10staff", "t10sta", "stat10"]
        self.stafft11=["stafft11", "t11staff", "t11sta", "stat11"]
        #Tiered Swords
        self.swordt1=["swordt1", "t1sword", "t1swo", "swot1"]
        self.swordt2=["swordt2", "t2sword", "t2swo", "swot2"]
        self.swordt3=["swordt3", "t3sword", "t3swo", "swot3"]
        self.swordt4=["swordt4", "t4sword", "t4swo", "swot4"]
        self.swordt5=["swordt5", "t5sword", "t5swo", "swot5"]
        self.swordt6=["swordt6", "t6sword", "t6swo", "swot6"]
        self.swordt7=["swordt7", "t7sword", "t7swo", "swot7"]
        self.swordt8=["swordt8", "t8sword", "t8swo", "swot8"]
        self.swordt9=["swordt9", "t9sword", "t9swo", "swot9"]
        self.swordt10=["swordt10", "t10sword", "t10swo", "swot10"]
        self.swordt11=["swordt11", "t11sword", "t11swo", "swot11"]
        #Elytras
        self.belytra=["belytra", "bronzeelytra", "elytrat1", "t1elytra"]
        self.selytra=["selytra", "silverelytra", "elytrat2", "t2elytra"]
        self.gelytra=["gelytra", "goldelytra", "elytrat3", "t3elytra"]
        self.pelytra=["pelytra", "platelytra", "platinumelytra", "elytrat4", "t4elytra"]
        self.delytra=["delytra", "diamondelytra", "diaelytra", "elytrat5", "t5elytra"]
        self.oelytra=["oelytra", "obsidianelytra", "obelytra", "elytrat6", "t6elytra"]
        self.brelytra=["brelytra", "bedrockelytra", "brocklytra", "elytrat7", "t7elytra"]
        #Exalted Armours
        self.ebplate=["exaltedbplate", "ebplate", "ebreastplateofnewlife"]
        self.ellegs=["exllegs", "ellegs", "elchaps", "elightningchaps"]
        self.echood=["echood", "exchood", "exaltedchood", "ehoodofthecultist"]
        self.esmask=["esmask", "exsmask", "exaltedsmask", "emaskofshaitan"]
        self.essandals=["essandals", "exssandals", "exaltedssandals", "espookysandals"]
        self.elboots=["elboots", "exlboots", "exaltedlboots", "elightningboots"]
        self.ecrobe=["ecrobe", "excrobe", "exaltedcrobe", "erobeofchronos"]
        self.eflegs=["eflegs", "exflegs", "exaltedflegs", "efrostleggings"]
        self.efboots=["efboots", "exfboots", "exaltedfboots", "efungalboots"]
        self.eoboots=["eoboots", "eonyxboots", "exoboots", "exaltedoboots", "eonyxsboots"]
        self.eochest=["eochest", "eonyxchest", "exochest", "exaltedochest", "eonyxschestplate"]
        self.eochaps=["eochaps", "eonyxchaps", "exochaps", "exaltedochaps", "eonyxschaps"]
        self.ecgreaves=["ecgreaves", "ecrayfishgreaves"]
        self.esarmour=["esarmour", "exsamour", "esarmor", "exsarmor", "escloth", "espectralclotharmour"]
        self.evhat=["evhat", "exvhat", "evoidhat"]
        self.esvisor=["esvisor", "exsvisor", "evisor", "esentinelsvisor"]
        self.ethood=["ethood", "exthood", "etwilight", "etwilighthood"]
        self.ecrown=["ecrown", "excrown", "exaltedcrown", "eforgottencrown", "etheforgottencrown"]
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
        self.cbow=["cbow", "coralbow", "bowofcorals"]
        self.ecbow=["ecbow", "excbow", "ecoralbow", "excoralbow", "ebowofcorals"]
        self.lbow=["lbow", "lightningbow", "lightbow"]
        self.elbow=["elbow", "exlbow", "exlightningbow", "elightningbow", "elightbow", "exlightbow"]
        self.bbow=["bbow", "blunderbow"]
        self.ebbow=["ebbow", "eblunderbow", "exbbow", "exblunderbow"]
        self.obow=["obow", "onyxbow", "olbow", "onyxlongbow"]
        self.eobow=["eobow", "exobow", "eonyxbow", "exonyxbow", "eolbow", "exolbow", "eonyxlongbow", "exonyxlongbow"]
        #UT Daggers 
        self.sdagger=["sdagger", "spiritdagger", "sdag"]
        self.esdagger=["esdagger", "esdag", "espiritdagger"]
        self.cdirk=["cdirk", "dirkofchronos"]
        self.ecdirk=["ecdirk", "excdirk", "edirkofchronos"]
        self.ddagger=["ddagger", "demonicdagger", "demdagger"]
        self.eddagger=["eddagger", "exddagger"]
        self.gdagger=["gdagger", "grassdagger", "cgdagger", "crossdagger", "crossgrassdagger"]
        self.egdagger=["egdagger", "egrassdagger", "ecgdagger", "ecrossdagger", "ecrossgrassdagger"]
        self.odagger=["odagger", "ocutter", "onyxdagger", "onyxcutter"]
        self.eodagger=["eodagger", "eocutter", "eonyxdagger", "eonyxcutter"]
        #UT Staves
        self.shovel=["gshovel", "gravediggers", "shovel", "gravediggersshovel"]
        self.eshovel=["egshovel", "egravediggers", "eshovel", "egravediggersshovel"]
        self.cultstaff=["cultstaff", "cstaff", "sacstaff", "unholystaff", "staffofunholysacrifice"]
        self.ecultstaff=["ecultstaff", "ecstaff", "esacstaff", "eunholystaff", "estaffofunholysacrifice"]
        self.crystalstaff=["crystalstaff", "crystaff", "crstaff", "crystallisedstaff"]
        self.ecrystalstaff=["ecrystalstaff", "ecrystaff", "ecrstaff", "ecrystallisedstaff"]
        self.asteroid=["asteroid", "asteroidstaff", "asterstaff"]
        self.easteroid=["easteroid", "easteroidstaff", "easterstaff"]
        self.ostaff=["ostaff", "oscythe", "onyxstaff", "onyxscythe"]
        self.eostaff=["eostaff", "eoscythe", "eonyxstaff", "eonyxscythe"]
        #UT Swords
        self.cutlass=["cutlass", "cut", "ghostkingscutlass"]
        self.ecutlass=["ecutlass", "ecut", "eghostkingscutlass"]
        self.dblade=["dblade", "demonblade", "demonicblade"]
        self.edblade=["edblade", "edemonblade", "edemonicblade"]
        self.gsword=["gsword", "asword", "guardiansword", "ancientsword", "swordoftheancientguardian"]
        self.egsword=["egsword", "easword", "eguardiansword", "eancientsword", "eswordoftheancientguardian"]
        self.tcleaver=["tcleaver", "cleaver", "titaniumcleaver"]
        self.etcleaver=["etcleaver", "ecleaver", "etitaniumcleaver"]
        self.osword=["osword", "onyxsword", "ogreatsword", "onyxgreatsword"]
        self.eosword=["eosword", "eonyxsword", "eogreatsword", "eonyxgreatsword"]
        #Orbs
        self.ot1=["orbt1", "t1orb"]
        self.ot2=["orbt2", "t2orb"]
        self.ot3=["orbt3", "t3orb"]
        self.ot4=["orbt4", "t4orb"]
        self.ot5=["orbt5", "t5orb"]
        self.conflict=["conflict", "orbofconflict"]
        self.econflict=["econflict", "eorbofconflict"]
        self.sorb=["sloworb", "sorb", "storb", "slowtouchorb"]
        self.esorb=["esloworb", "esorb", "estorb", "eslowtouchorb"]
        #Cloaks
        self.ct1=["cloakt1", "t1cloak"]
        self.ct2=["cloakt2", "t2cloak"]
        self.ct3=["cloakt3", "t3cloak"]
        self.ct4=["cloakt4", "t4cloak"]
        self.ct5=["cloakt5", "t5cloak"]
        self.bcloak=["bcloak", "bloodycloak"]
        self.ebcloak=["ebcloak", "ebloodycloak"]
        self.ccloak=["ccloak", "combustioncloak"]
        self.eccloak=["eccloak", "ecombustioncloak"]
        #Helmets
        self.het1=["helmett1", "t1helmet"]
        self.het2=["helmett2", "t2helmet"]
        self.het3=["helmett3", "t3helmet"]
        self.het4=["helmett4", "t4helmet"]
        self.het5=["helmett5", "t5helmet"]
        self.jugg=["jug", "jugg", "helmetofthejuggernaut"]
        self.ejugg=["ejug", "ejugg", "ehelmetofthejuggernaut"]
        self.ehelm=["ehelm", "ehelmet", "helmetoftheelements"]
        self.eehelm=["eehelm", "eehelmet", "ehelmetoftheelements"]
        #Poisons
        self.pt1=["poisont1", "t1poison"]
        self.pt2=["poisont2", "t2poison"]
        self.pt3=["poisont3", "t3poison"]
        self.pt4=["poisont4", "t4poison"]
        self.pt5=["poisont5", "t5poison"]
        self.ppoison=["ppoison", "plaguepoison"]
        self.eppoison=["eppoison", "eplaguepoison"]
        self.cfang=["cfang", "fpoison", "fangpoison", "crystallisedfang", "crystallisedfangpoison"]
        self.ecfang=["ecfang", "efpoison", "efangpoison", "ecrystallisedfang", "ecrystallisedfangpoison"]
        #Shields
        self.st1=["shieldt1", "t1shield"]
        self.st2=["shieldt2", "t2shield"]
        self.st3=["shieldt3", "t3shield"]
        self.st4=["shieldt4", "t4shield"]
        self.st5=["shieldt5", "t5shield"]
        self.cshield=["cshield", "crystalshield"]
        self.ecshield=["ecshield", "ecrystalshield"]
        self.ogmur=["ogmur", "shieldofogmur"]
        self.eogmur=["eogmur", "eshieldofogmur"]
        #Skulls
        self.skt1=["skullt1", "t1skull"]
        self.skt2=["skullt2", "t2skull"]
        self.skt3=["skullt3", "t3skull"]
        self.skt4=["skullt4", "t4skull"]
        self.skt5=["skullt5", "t5skull"]
        self.sskull=["sskull", "shaitanskull", "shaitansskull"]
        self.esskull=["esskull", "eshaitanskull", "eshaitanskull"]
        self.heart=["heart", "heartofchronos", "cheart"]
        self.eheart=["eheart", "eheartofchronos", "echeart"]
        #Traps
        self.tt1=["trapt1", "t1trap"]
        self.tt2=["trapt2", "t2trap"]
        self.tt3=["trapt3", "t3trap"]
        self.tt4=["trapt4", "t4trap"]
        self.tt5=["trapt5", "t5trap"]
        self.ctrap=["ctrap", "crystaltrap"]
        self.ectrap=["ectrap", "ecrystaltrap"]
        self.cotrap=["cotrap", "coraltrap", "trapofcorals"]
        self.ecotrap=["ecotrap", "ecoraltrap", "etrapofcorals"]
        #Stars
        self.stt1=["start1", "t1star"]
        self.stt2=["start2", "t2star"]
        self.stt3=["start3", "t3star"]
        self.stt4=["start4", "t4star"]
        self.stt5=["start5", "t5star"]
        self.cstar=["cstar", "starofconflict", "conflictstar"]
        self.ecstar=["ecstar", "estarofconflict", "econflictstar"]
        self.estar=["estar", "elementalstar", "starofelements", "staroftheelements"]
        self.eestar=["eestar", "eelementalstar", "estarofelements", "estaroftheelements"]
        #Kunais
        self.kt1=["kunait1", "t1kunai"]
        self.kt2=["kunait2", "t2kunai"]
        self.kt3=["kunait3", "t3kunai"]
        self.kt4=["kunait4", "t4kunai"]
        self.kt5=["kunait5", "t5kunai"]
        self.fkunai=["fkunai", "frozenkunai"]
        self.efkunai=["efkunai", "efrozenkunai"]
        self.ckunai=["ckunai", "crystallizedkunai"]
        self.eckunai=["ckunai", "ecrystallizedkunai"]
        print('Wiki intisialised')

    @commands.command(aliases=["wiki"])
    async def info(self, ctx, *, terms):
        terms=terms.lower()
        terms = terms.replace(" ", "")
        terms=re.sub(r'\W+', '', terms)
        await ctx.message.delete()
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
        #Tiered Heavy Armours
        elif terms in self.ht11:
            terms = "ht11"
        elif terms in self.ht10:
            terms = "ht10"
        elif terms in self.ht9:
            terms = "ht9"
        elif terms in self.ht8:
            terms = "ht8"
        elif terms in self.ht7:
            terms = "ht7"
        elif terms in self.ht6:
            terms = "ht6"
        elif terms in self.ht5:
            terms = "ht5"
        elif terms in self.ht4:
            terms = "ht4"
        elif terms in self.ht3:
            terms = "ht3"
        elif terms in self.ht2:
            terms = "ht2"
        elif terms in self.ht1:
            terms = "ht1"
        #Tiered Leather Armours
        elif terms in self.lt11:
            terms = "lt11"
        elif terms in self.lt10:
            terms = "lt10"
        elif terms in self.lt9:
            terms = "lt9"
        elif terms in self.lt8:
            terms = "lt8"
        elif terms in self.lt7:
            terms = "lt7"
        elif terms in self.lt6:
            terms = "lt6"
        elif terms in self.lt5:
            terms = "lt5"
        elif terms in self.lt4:
            terms = "lt4"
        elif terms in self.lt3:
            terms = "lt3"
        elif terms in self.lt2:
            terms = "lt2"
        elif terms in self.lt1:
            terms = "lt1"
        #Tiered Robe Armours
        elif terms in self.rt11:
            terms = "rt11"
        elif terms in self.rt10:
            terms = "rt10"
        elif terms in self.rt9:
            terms = "rt9"
        elif terms in self.rt8:
            terms = "rt8"
        elif terms in self.rt7:
            terms = "rt7"
        elif terms in self.rt6:
            terms = "rt6"
        elif terms in self.rt5:
            terms = "rt5"
        elif terms in self.rt4:
            terms = "rt4"
        elif terms in self.rt3:
            terms = "rt3"
        elif terms in self.rt2:
            terms = "rt2"
        elif terms in self.rt1:
            terms = "rt1"
        #Tiered Katanas
        elif terms in self.katt1:
            terms="katt1"
        elif terms in self.katt2:
            terms="katt2"
        elif terms in self.katt3:
            terms="katt3"
        elif terms in self.katt4:
            terms="katt4"
        elif terms in self.katt5:
            terms="katt5"
        elif terms in self.katt6:
            terms="katt6"
        elif terms in self.katt7:
            terms="katt7"
        elif terms in self.katt8:
            terms="katt8"
        elif terms in self.katt9:
            terms="katt9"
        elif terms in self.katt10:
            terms="katt10"
        elif terms in self.katt11:
            terms="katt11"
                #Tiered Katanas
        #Tiered Bows
        elif terms in self.bowt1:
            terms="bowt1"
        elif terms in self.bowt2:
            terms="bowt2"
        elif terms in self.bowt3:
            terms="bowt3"
        elif terms in self.bowt4:
            terms="bowt4"
        elif terms in self.bowt5:
            terms="bowt5"
        elif terms in self.bowt6:
            terms="bowt6"
        elif terms in self.bowt7:
            terms="bowt7"
        elif terms in self.bowt8:
            terms="bowt8"
        elif terms in self.bowt9:
            terms="bowt9"
        elif terms in self.bowt10:
            terms="bowt10"
        elif terms in self.bowt11:
            terms="bowt11"
        #Tiered Daggers
        elif terms in self.daggert1:
            terms="daggert1"
        elif terms in self.daggert2:
            terms="daggert2"
        elif terms in self.daggert3:
            terms="daggert3"
        elif terms in self.daggert4:
            terms="daggert4"
        elif terms in self.daggert5:
            terms="daggert5"
        elif terms in self.daggert6:
            terms="daggert6"
        elif terms in self.daggert7:
            terms="daggert7"
        elif terms in self.daggert8:
            terms="daggert8"
        elif terms in self.daggert9:
            terms="daggert9"
        elif terms in self.daggert10:
            terms="daggert10"
        elif terms in self.daggert11:
            terms="daggert11"
        #Tiered Staves
        elif terms in self.stafft1:
            terms="stafft1"
        elif terms in self.stafft2:
            terms="stafft2"
        elif terms in self.stafft3:
            terms="stafft3"
        elif terms in self.stafft4:
            terms="stafft4"
        elif terms in self.stafft5:
            terms="stafft5"
        elif terms in self.stafft6:
            terms="stafft6"
        elif terms in self.stafft7:
            terms="stafft7"
        elif terms in self.stafft8:
            terms="stafft8"
        elif terms in self.stafft9:
            terms="stafft9"
        elif terms in self.stafft10:
            terms="stafft10"
        elif terms in self.stafft11:
            terms="stafft11"
        #Tiered Swords
        elif terms in self.swordt1:
            terms="swordt1"
        elif terms in self.swordt2:
            terms="swordt2"
        elif terms in self.swordt3:
            terms="swordt3"
        elif terms in self.swordt4:
            terms="swordt4"
        elif terms in self.swordt5:
            terms="swordt5"
        elif terms in self.swordt6:
            terms="swordt6"
        elif terms in self.swordt7:
            terms="swordt7"
        elif terms in self.swordt8:
            terms="swordt8"
        elif terms in self.swordt9:
            terms="swordt9"
        elif terms in self.swordt10:
            terms="swordt10"
        elif terms in self.swordt11:
            terms="swordt11"
        #Elytras
        elif terms in self.belytra:
            terms="belytra"
        elif terms in self.selytra:
            terms="selytra"
        elif terms in self.pelytra:
            terms="pelytra"
        elif terms in self.gelytra:
            terms="gelytra"
        elif terms in self.delytra:
            terms="delytra"
        elif terms in self.oelytra:
            terms="oelytra"
        elif terms in self.brelytra:
            terms="brelytra"
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
        elif terms in self.het1:
            terms="het1"
        elif terms in self.het2:
            terms="het2"
        elif terms in self.het3:
            terms="het3"
        elif terms in self.het4:
            terms="het4"
        elif terms in self.het5:
            terms="het5"
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
        #Shield
        elif terms in self.st1:
            terms="st1"
        elif terms in self.st2:
            terms="st2"
        elif terms in self.st3:
            terms="st3"
        elif terms in self.st4:
            terms="st4"
        elif terms in self.st5:
            terms="st5"
        elif terms in self.cshield:
            terms="cshield"
        elif terms in self.ecshield:
            terms="ecshield"
        elif terms in self.ogmur:
            terms="ogmur"
        elif terms in self.eogmur:
            terms="eogmur"
        #Skulls
        elif terms in self.skt1:
            terms="skt1"     
        elif terms in self.skt2:
            terms="skt2"  
        elif terms in self.skt3:
            terms="skt3"  
        elif terms in self.skt4:
            terms="skt4"  
        elif terms in self.skt5:
            terms="skt5"     
        elif terms in self.sskull:
            terms="sskull"
        elif terms in self.esskull:
            terms="esskull"
        elif terms in self.heart:
            terms="heart"
        elif terms in self.eheart:
            terms="eheart"
        #Traps
        elif terms in self.tt1:
            terms="tt1"
        elif terms in self.tt2:
            terms="tt2"
        elif terms in self.tt3:
            terms="tt3"
        elif terms in self.tt4:
            terms="tt4"
        elif terms in self.tt5:
            terms="tt5"
        elif terms in self.ctrap:
            terms="ctrap"
        elif terms in self.ectrap:
            terms="ectrap"
        elif terms in self.cotrap:
            terms="cotrap"
        elif terms in self.ecotrap:
            terms="ecotrap"
        #Stars
        elif terms in self.stt1:
            terms="stt1"
        elif terms in self.stt2:
            terms="stt2"
        elif terms in self.stt3:
            terms="stt3"
        elif terms in self.stt4:
            terms="stt4"
        elif terms in self.stt5:
            terms="stt5"
        elif terms in self.cstar:
            terms="cstar"
        elif terms in self.ecstar:
            terms="ecstar"
        elif terms in self.estar:
            terms="estar"
        elif terms in self.eestar:
            terms="eestar"
        #Kunais
        elif terms in self.kt1:
            terms="kt1"
        elif terms in self.kt2:
            terms="kt2"
        elif terms in self.kt3:
            terms="kt3"
        elif terms in self.kt4:
            terms="kt4"
        elif terms in self.kt5:
            terms="kt5"
        elif terms in self.fkunai:
            terms="fkunai"
        elif terms in self.efkunai:
            terms="efkunai"
        elif terms in self.ckunai:
            terms="ckunai"
        elif terms in self.eckunai:
            terms="eckunai"
        if terms in ["warrior", "knight", "necro", "battlemage", "huntress", "assassin", "rogue", "ninja", "samurai"]:
            with open(r'rotmc.json') as f:
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
            with open(r'rotmc.json') as f:
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
            with open(r'rotmc.json') as f:
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
            with open(r'rotmc.json') as f:
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
        elif terms in ["ot1", "ot2", "ot3", "ot4", "ot5", "conflict", "econflict", "sorb", "esorb", "ct1", "ct2", "ct3", "ct4", "ct5", "bcloak", "ebcloak", "ccloak", "eccloak", "het1", "het2", "het3", "het4", "het5", "jugg", "ejugg", "ehelm", "eehelm", "pt1", "pt2", "pt3", "pt4", "pt5", "ppoison", "eppoison", "cfang", "ecfang", "st1", "st2", "st3", "st4", "st5", "cshield", "ecshield", "ogmur", "eogmur", "skt1", "skt2", "skt3", "skt4", "skt5", "sskull", "esskull", "heart", "eheart", "tt1", "tt2", "tt3", "tt4", "tt5", "ctrap", "ectrap", "cotrap", "ecotrap", "stt1", "stt2", "stt3", "stt4", "stt5", "cstar", "ecstar", "estar", "eestar", "kt1", "kt2", "kt3", "kt4", "kt5", "fkunai", "efkunai", "ckunai", "eckunai"]:
            with open(r'rotmc.json') as f:
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
        elif terms in ["ht11", "ht10", "ht9", "ht8", "ht7", "ht6", "ht5", "ht4", "ht3", "ht2", "ht1", "lt11", "lt10", "lt9", "lt8", "lt7", "lt6", "lt5", "lt4", "lt3", "lt2", "lt1", "rt11", "rt10", "rt9", "rt8", "rt7", "rt6", "rt5", "rt4", "rt3", "rt2", "rt1"]:
            with open(r'rotmc.json') as f:
                f = json.load(f)
                data=f["items"][terms]
                tpe=data["type"]
                gem=data["gem"]
                lreq=data["lreq"]
                stats=data["stats"]
                stats=', '.join(stats)
                classes=data["classes"]
                classes=', '.join(classes)
                tier=data["tier"]
                name=data["name"]
                colour=data["colour"]
                tn=data["tn"]
                em=embeds.tarmours(tpe, gem, lreq, stats, classes, tier, name, colour, tn)
                await ctx.send(embed=em)
        elif terms in ["katt1", "katt2", "katt3", "katt4", "katt5", "katt6", "katt7", "katt8", "katt9", "katt10", "katt11", "bowt1", "bowt2", "bowt3", "bowt4", "bowt5", "bowt6", "bowt7", "bowt8", "bowt9", "bowt10", "bowt11", "daggert1", "daggert2", "daggert3", "daggert4", "daggert5", "daggert6", "daggert7", "daggert8", "daggert9", "daggert10", "daggert11", "stafft1", "stafft2", "stafft3", "stafft4", "stafft5", "stafft6", "stafft7", "stafft8", "stafft9", "stafft10", "stafft11", "swordt1", "swordt2", "swordt3", "swordt4", "swordt5", "swordt6", "swordt7", "swordt8", "swordt9", "swordt10", "swordt11"]:
            with open(r'rotmc.json') as f:
                f = json.load(f)
                data=f["items"][terms]
                tpe=data["type"]
                damage=data["damage"]
                rge=data["range"]
                shots=data["shots"]
                velocity=data["velocity"]
                pierces=data["pierces"]
                cd=data["cd"]
                lreq=data["lreq"]
                classes=data["classes"]
                classes=', '.join(classes)
                name=data["name"]
                gem=data["gem"]
                tier=data["tier"]
                colour=data["colour"]
                tn=data["tn"]
                em=embeds.tweapons(tpe, damage, rge, shots, velocity, pierces, cd, lreq, classes, name, gem, tier, colour, tn)
                await ctx.send(embed=em)
        elif terms in ["belytra", "selytra", "gelytra", "pelytra", "delytra", "oelytra", "brelytra"]:
            with open(r'rotmc.json') as f:
                f = json.load(f)
                data=f["items"][terms]
                name=data["name"]
                defense=data["defense"]
                attack=data["attack"]
                speed=data["speed"]
                dodge=data["dodge"]
                health=data["health"]
                gem=data["gem"]
                colour=data["colour"]
                tn=data["tn"]
                em=embeds.elytras(defense, attack, speed, dodge, health, gem, name, colour, tn)
                await ctx.send(embed=em)
        elif terms == "gems":
            paginator = Paginator(pages=self.get_pages())
            await paginator.start(ctx)
        else:
            await ctx.send(f"couldn't find {terms} in the database, please try again")

    def get_pages(self):
        pages = []
        #Index
        embed=discord.Embed(
            title="**Gem Index Page**"
        )
        embed.add_field(
            name="**Controls**",
            value="`Skip To A Page:` :1234: \n `Forward One:` :arrow_forward: \n `Backword One:` :arrow_backward: \n `Skip To End:` :track_next: \n `Go Back Here:` :track_previous: \n `Quit:` :stop_button:"
        )
        embed.add_field(
            name="**Index**",
            value="`Vitality Gems:` Page 2 \n `Speed Gems:` Page 3 \n `Evasion Gems:` Page 4 \n `Attack Gems:` Page 5 \n `Defense Gems:` Page 6 \n `Health Gems:` Page 7 \n `CritHit Gems:` Page 8 \n `CritDamage Gems:` Page 9"
        )
        embed.add_field(
            name="**Drop Locations**",
            value="`Tier 1 Gems:` Tutorial/Early Quests \n `Tier 2 Gems:` Purple Bags \n `Tier 3 Gems:` Blue Bags \n `Tier 4 Gems:` Blue Bags \n `Tier 5 Gems:` Blue Bags"
        )
        embed.color=discord.Color.random()
        pages.append(embed)
        #Vit Gems
        embed=discord.Embed(
            title="**Topaz of Vitality**",
            description="""
            <:vitalityt1:838121456730505257> Topaz of Vitality I: `+0.01 HP/s`
                    <:vitalityt2:838121456831037461> Topaz of Vitality II: `+0.02 HP/s`
                    <:vitalityt3:838121456642424853> Topaz of Vitality III: `+0.03 HP/s`
                    <:vitalityt4:838121456709402714> Topaz of Vitality IV: `+0.04 HP/s`
                    <:vitalityt5:838121456314351678> Topaz of Vitality V: `+0.05 HP/s`"""
        )
        embed.color=discord.Color.random()
        pages.append(embed)
        #Speed Gems
        embed=discord.Embed(
            title="**Emerald of Speed**",
            description="""
            <:speedt1:838121339352645643> Emerald of Speed I: `+0.5% Speed`
                     <:speedt2:838121339490402334> Emerald of Speed II: `+1% Speed`
                     <:speedt3:838121339533000754> Emerald of Speed III: `+1.5% Speed`
                     <:speedt4:838121339536539729> Emerald of Speed IV: `+2% Speed`
                     <:speedt5:838121339633139742> Emerald of Speed V: `+2.5% Speed`"""
        )
        embed.color=discord.Color.random()
        pages.append(embed)
        #Evasion Gems
        embed=discord.Embed(
            title="**Crystal of Evasion**",
            description="""<:evasiont1:838121191775535124> Crystal of Evasion I: `+0.5% Evasion`
                           <:evasiont2:838121191780384848> Crystal of Evasion II: `+1% Evasion`
                           <:evasiont3:838121191780253706> Crystal of Evasion III: `+1.5% Evasion`
                           <:evasiont4:838121191876984942> Crystal of Evasion IV: `+2% Evasion`
                           <:evasiont5:838121191784579072> Crystal of Evasion V: `+2.5% Evasion`"""
        )
        embed.color=discord.Color.random()
        pages.append(embed)
        #Attack Gems
        embed=discord.Embed(
            title="**Diamond of Attack**",
            description="""<:attackt1:838120894332665856> Diamond of Attack I: `+0.5% Attack`
                    <:attackt2:838120894320738324> Diamond of Attack II: `+1% Attack`
                    <:attackt3:838120894538579978> Diamond of Attack III: `+1.5% Attack`
                    <:attackt4:838120893925949481> Diamond of Attack IV: `+2% Attack`
                    <:attackt5:838120894076813313> Diamond of Attack V: `+2.5% Attack`"""
        )
        embed.color=discord.Color.random()
        pages.append(embed)
        #Defense Gems
        embed=discord.Embed(
            title="**Sapphire of Defense**",
            description="""<:defenset1:838121072838049832> Sapphire of Defense I: `+0.5% Defense`
                    <:defenset2:838121073001103360> Sapphire of Defense II: `+1% Defense`
                    <:defenset3:838121072469213185> Sapphire of Defense III: `+1.5% Defense`
                    <:defenset4:838121073056677908> Sapphire of Defense IV: `+2% Defense`
                    <:defenset5:838121072909221898> Sapphire of Defense V: `+2.5% Defense`"""
        )
        embed.color=discord.Color.random()
        pages.append(embed)
        #Health Gems
        embed=discord.Embed(
            title="**Ruby of Health**",
            description="""<:lifet1:838388315500838973> Ruby of Health I: `+0.5 Health`
                    <:lifet2:838388333633732648> Ruby of Health II: `+1 Health`
                    <:lifet3:838388347222491196> Ruby of Health III: `+1.5 Health`
                    <:lifet4:838388359326859338> Ruby of Health IV: `+2 Health`
                    <:lifet5:838388370514116638> Ruby of Health V: `+2.5 Health`"""
        )
        embed.color=discord.Color.random()
        pages.append(embed)
        #CritHit Gems
        embed=discord.Embed(
            title="**Amethyst of CritHit**",
            description="""<:crithitt1:838120999215169577> Amethyst of CritHit I: `+0.5% CritHit`
                    <:crithitt2:838120999429341185> Amethyst of CritHit II: `+1% CritHit`
                    <:crithitt3:838120999395917865> Amethyst of CritHit III: `+1.5% CritHit`
                    <:crithitt4:838120999340736549> Amethyst of CritHit IV: `+2% CritHit`
                    <:crithitt5:838120998926155818> Amethyst of CritHit V: `+2.5% CritHit`"""
        )
        embed.color=discord.Color.random()
        pages.append(embed)
        #CritDamage Gems
        embed=discord.Embed(
            title="**Almandine of CritDamage**",
            description="""<:critdamaget1:838120998997196801> Almandine of CritDamage I: `+0.5% CritDamage`
                    <:critdamaget2:838120999312031794> Almandine of CritDamage II: `+1% CritDamage`
                    <:critdamaget3:838120999001260084> Almandine of CritDamage III: `+1.5% CritDamage`
                    <:critdamaget4:838120999333265428> Almandine of CritDamage IV: `+2% CritDamage`
                    <:critdamaget5:838120999413219348> Almandine of CritDamage V: `+2.5% CritDamage`"""
        )
        embed.color=discord.Color.random()
        pages.append(embed)
        return pages
    

def setup(client):
    client.add_cog(Wiki(client))