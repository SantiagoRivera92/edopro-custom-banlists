import urllib.request, json, operator
from datetime import datetime
header= {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) ' 
			'AppleWebKit/537.11 (KHTML, like Gecko) '
			'Chrome/23.0.1271.64 Safari/537.11',
			'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
			'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
			'Accept-Encoding': 'none',
			'Accept-Language': 'en-US,en;q=0.8',
			'Connection': 'keep-alive'}
url = "https://db.ygoprodeck.com/api/v7/cardinfo.php"
request = urllib.request.Request(url, None, header)

additionalForbidden = [
		"There Can Be Only One",
		"Artifact Scythe"
		]
additionalLimited = []
additionalSemiLimited = []
additionalUnlimited = [
	"Diamond Dire Wolf",
	"Number S39: Utopia the Lightning", 
	"Gladiator Beast Augustus", 
	"Gladiator Beast Retiari", 
	"Gladiator Beast Gyzarus",
	"Test Panther",
	"Gladiator Beast Andabata",
	"Gladiator Beast Domitianus",
	"Koa'ki Meiru Urnight",
	"Shiranui Spectralsword",
	"Vision HERO Vyon",
	"Shiranui Shogunsaga",
	"Traptrix Myrmeleo",
	"Traptrix Dionaea",
	"Traptrix Mantis",
	"Ghostrick Alucard",
	"Brotherhood of the Fire Fist - Bear",
	"Shiranui Sunsaga",
	"Necrovalley Throne",
	"Wind-Up Zenmaines",
	"Heroic Challenger - Assault Halberd",
	"Evolzar Dolkka",
	"Gachi Gachi Gantetsu",
	"Number 101: Silent Honor ARK",
	"Master Hyperion",
	"The Agent of Miracles - Jupiter",
	"The Agent of Mystery - Earth",
	"The Agent of Life - Neptune",
	"The Executor of the Underworld - Pluto",
	"Protector of The Agents - Moon",
	"The Sacred Waters in the Sky",
	"Salamangreat Spinny",
	"Salamangreat Balelynx",
	"Salamangreat Circle",
	"Bujin Hiruko",
	"Bujin Hirume",
	"Bujin Mikazuchi",
	"Bujingi Peacock",
	"Bujin Yamato",
	"Bujingi Crow",
	"Bujingi Hare",
	"Bujin Arasuda",
	"Bujingi Quilin",
	"Bujingi Crane",
	"Bujintei Susanowo",
	"Bujintei Kagutsuchi",
	"Bujincarnation",
	"Springans Ship - Exblowrer",
	"Springans Merrymaker",
	"Springans Watch",
	"Great Sand Sea - Gold Golgonda",
	"Pacifis, the Phantasm City",
	"Phantasm Spiral Battle",
	"Marincess Blue Slug",
	"Marincess Coral Anemone",
	"U.A. Hyper Stadium",
	"Altergeist Meluseek",
	"Battlin' Boxer Lead Yoke",
	"Digital Bug Rhinosebus",
	"Impcantation Candoll",
	"Impcantation Chalislime",
	"Infinitrack Trencher",
	"Infinitrack Anchor Drill",
	"Infinitrack River Stormer",
	"Infinitrack Goliath",
	"Heavy Forward",
	"Koa'ki Meiru Maximus",
	"Koa'ki Meiru Wall",
	"Iron Core Specimen Lab",
	"Starlight Road",
	"Magical Musketeer Wild",
	"Magical Musketeer Calamity",
	"Magical Musketeer Starfire",
	"Magical Musketeer Kidbrave",
	"Magical Musketeer Doc",
	"Magical Musketeer Caspar",
	"Magical Musket - Steady Hands",
	"Magical Musket - Cross-Domination",
	"Magical Musket - Desperado",
	"Magical Musket - Dancing Needle",
	"Magical Musket - Fiendish Deal",
	"Magical Musket - Last Stand",
	"Gladiator Beast Noxious",
	"Megalith Ophiel",
	"Mermail Abyssleed",
	"Mermail Abyssmegalo",
	"Mermail Abyssteus",
	"Mermail Abyssturge",
	"Mermail Abysspike",
	"Mermail Abyssmander",
	"Mermail Abysslinde",
	"Mermail Abyssgunde",
	"Mermail Abyssgaios",
	"Mermail Abyssalacia",
	"Mermail Abysstrite",
	"Abyss-squall",
	"Abyss-sphere",
	"Myutant Arsenal",
	"Myutant Mist",
	"Myutant Beast",
	"Myutant ST-46",
	"Myutant M-05",
	"Myutant Synthesis",
	"Myutant Evolution Lab",
	"Gladiator Rejection",
	"Abyss Shark",
	"Crystal Shark",
	"Double Fin Shark",
	"Valiant Shark Lancer",
	"Beautunaful Princess",
	"Silent Sea Nettle",
	"Bahamut Shark",
	"Number 37: Hope Woven Dragon Spider Shark",
	"Number 70: Malevolent Sin",
	"Number 47: Nightmare Shark",
	"Satellarknight Rigel",
	"Satellarknight Altair",
	"Satellarknight Sirius",
	"Satellarknight Deneb",
	"Satellarknight Alsahm",
	"Stellarknight Triverr",
	"Stellarknight Delteros",
	"Satellarknight Skybridge",
	"Tellarknight Genesis",
	"Stellarnova Alpha",
	"The Phantom Knights of Break Sword",
	"Time Thief Adjuster",
	"Time Thief Temporwhal",
	"Time Thief Double Barrel",
	"Time Thief Perpetua",
	"Thunder Dragonduo",
	"Thunder Dragondark",
	"Thunder Dragonroar",
	"Thunder Dragonhawk",
	"Thunder Dragon Thunderstormech",
	"Some Summer Summoner",
	"Batteryman Industrial Strength",
	"Batteryman Fuel Cell",
	"Vampire Voivode",
	"Vampire Vamp",
	"Vampire Duke",
	"Vampire Sorcerer",
	"Vampire Ghost",
	"Crimson Knight Vampire Bram",
	"Vampire Fascinator",
	"Vampire Takeover",
	"Vampire Sucker",
	"Wattgiraffe",
	"Watthydra",
	"Wattchimera",
	"Wattcastle",
	"Suanni, Fire of the Yang Zing",
	"Bi'an, Earth of the Yang Zing",
	"Bixi, Water of the Yang Zing",
	"Jiaotu, Darkness of the Yang Zing",
	"Pulao, Wind of the Yang Zing",
	"Chiwen, Light of the Yang Zing",
	"Yang Zing Path",
	"Yang Zing Creation",
	"Nine Pillars of Yang Zing",
	"Beat, Bladesman Fur Hire",
	"Filo, Messenger Fur Hire",
	"Folgo, Justice Fur Hire",
	"XX-Saber Gardestrike",
	"XX-Saber Garsem",
	"XX-Saber Emmersblade",
	"XX-Saber Darksoul",
	"XX-Saber Gottoms",
	"XX-Saber Hyunlei",
	"Saber Slash",
	"Gottoms' Second Call",
	"Saber Vault",
	"Saber Hole",
	"Karakuri Muso mdl 818 \"Haipa\"",
	"Karakuri Bushi mdl 6318 \"Muzanichiha\"",
	"Karakuri Ninja mdl 339 \"Sazank\"",
	"Karakuri Merchant mdl 177 \"Inashichi\"",
	"Karakuri Barrel mdl 96 \"Shinkuro\"",
	"Karakuri Shogun mdl 00 \"Burei\"",
	"Karakuri Super Shogun mdl 00N \"Bureibu\"",
	"Shiranui Squire",
	"Gadarla, the Mystery Dust Kaiju",
	"Gameciel, the Sea Turtle Kaiju",
	"Kumongous, the Sticky String Kaiju",
	"Blackwing - Simoon the Poison Wind",
	"Blackwing - Kris the Crack of Dawn",
	"Blackwing - Gale the Whirlwind",
	"Blackwing - Vayu the Emblem of Honor",
	"Blackwing Armor Master",
	"Assault Blackwing - Raikiri the Rain Shower",
	"Blackwing - Silverwind the Ascendant",
	"Blackwing Full Armor Master",
	"Assault Blackwing - Onimaru the Divine Thunder",
	"Orient Dragon",
	"Stardust Charge Warrior",
	"Thought Ruler Archfiend",
	"Mist Wurm",
	"Virtual World Beast - Jiujiu",
	"Virtual World Phoenix - Fanfan",
	"Fabled Andwraith",
	"Chronomaly City Babylon",
	"Chronomaly Crystal Chrononaut",
	"Number 36: Chronomaly Chateau Huyuk",
	"Chronomaly Gordian Knot",
	"Chronomaly Crystal Skull",
	"Chronomaly Cabrera Trebuchet",
	"Chronomaly Colossal Head",
	"Chronomaly Magella Globe",
	"Chronomaly Aztec Mask Golem",
	"Chronomaly Mud Golem",
	"Chronomaly Nebra Disk",
	"Chronomaly Tula Guardian",
	"Chronomaly Sol Monolith",
	"Triamid Sphinx",
	"Triamid Master",
	"Triamid Hunter",
	"Triamid Cruiser",
	"Triamid Kingolem",
	"Triamid Pulse",
	"Alpha The Electromagnet Warrior",
	"Beta The Electromagnet Warrior",
	"Gamma The Electromagnet Warrior",
	"Berserkion the Electromagna Warrior",
	"Magnet Induction",
	"Reptilianne Vaskii",
	"Reptilianne Melusine",
	"Reptilianne Ramifications",
	"Gallant Granite",
	"Mecha Phantom Beast Dracossack",
	"PSY-Framelord Zeta",
	"Star Eater",
	"Celestial Observatory",
	"Yellow Dragon Ninja",
	"White Dragon Ninja",
	"Twilight Ninja Jogen",
	"Red Dragon Ninja",
	"Blue Dragon Ninja",
	"Yellow Ninja",
	"Ninja Grandmaster Hanzo",
	"Twilight Ninja Kagen",
	"Blade Armor Ninja",
	"Elemental HERO The Shining",
	"Elemental HERO Nova Master",
	"Ninja Grandmaster Saizo",
	"Hidden Village of Ninjitsu Arts",
	"Armor Ninjitsu Art of Rust Mist",
	"Ninjitsu Art of Duplication",
	"Ninjitsu Art of Mirage-Transformation",
	"Speedroid Rubberband Plane",
	"Hi-Speedroid Kitedrake",
	"Hi-Speedroid Hagoita",
	"Speedroid Scratch",
	"Speedroid Wheel",
	"Speedroid Dupligate",
	"Clear Wing Fast Dragon",
	"Clear Wing Synchro Dragon",
	"Fluffal Dog",
	"Fluffal Penguin",
	"Fluffal Owl",
	"Frightfur Wolf",
	"Frightfur Tiger",
	"Frightfur Sabre-Tooth",
	"Frightfur Kraken",
	"Suture Rebirth",
	"Evilswarm Ketos",
	"Evilswarm Castor",
	"Evilswarm Kerykeion",
	"Evilswarm Ophion",
	"Evilswarm Ouroboros",
	"Evilswarm Bahamut",
	"Constellar Pollux",
	"Constellar Caduceus",
	"Constellar Sombre",
	"Constellar Ptolemy M7",
	"Constellar Omega",
	"Wind-Up Shark",
	"Wind-Up Magician",
	"Wind-Up Rabbit",
	"Wind-Up Rat",
	"Wind-Up Arsenal Zenmaioh",
	"Wind-Up Zenmaintenance",
	"Inzektor Giga-Mantis",
	"Inzektor Hopper",
	"Inzektor Exa-Beetle",
	"Inzektor Exa-Stag",
	"Zektrike Kou-ou",
	"Artifact Sanctum",
	"Worm King",
	"Worm Zero",
	"Tindangle Dholes",
	"Tindangle Jhrelth",
	"Fusion Destiny"
	]

#(C) is common, (SP) is Short Print, (SSP) is Super Short Print, (DNPR) is Duel Terminal common
legalRarities = ['(C)', '(SP)', '(SSP)', '(DNPR)']

#Banlist status
banned = 'Banned'
limited = 'Limited'
semi = 'Semi-Limited'

#YGOPRODECK API keys
data = 'data'
card_sets = 'card_sets'
banlist_info = 'banlist_info'
ban_tcg = 'ban_tcg'
rarity_code = 'set_rarity_code'
card_images = 'card_images'
cardType = 'type'

#Token stuff
token = 'Token'

#My keys
name = 'name'
cardId = 'id'
status = 'status'

#Filename for banlist file
banlistFilename = 'banlist/cc++.lflist.conf'
siteFilename ='site/plus/banlist.md'

#Card arrays
siteCards = []
simpleCards = [] # List of all TCG legal cards for banlist generation
ocgCards = [] # List of all OCG exclusive cards for banlist generation.

def printAdditionalArrays():
	print("Did I misspell something?")
	print("Additional forbidden cards:")
	print(additionalForbidden)
	print("Additional limited cards:")
	print(additionalLimited)
	print("Additional semi-limited cards:")
	print(additionalSemiLimited)
	print("Additional unlimited cards:")
	print(additionalUnlimited)

def writeCardToBanlist(card, outfile):
	try:
		outfile.write("%d %d -- %s\n" % (card.get(cardId), card.get(status), card.get(name)))
	except TypeError:
		print(card)

def writeCardToSite(card, outfile):
	cardStatus = card.get(status)
	cardStatusAsText = "Unlimited"
	if (cardStatus == -1):
		cardStatusAsText = "Illegal"
	elif (cardStatus == 0):
		cardStatusAsText = "Forbidden"
	elif (cardStatus == 1):
		cardStatusAsText = "Limited"
	elif (cardStatus == 2):
		cardStatusAsText = "Semi-Limited"

	cardUrl = "https://db.ygoprodeck.com/card/?search=%s"%card.get(name).replace(" ", "%20").replace("&", "%26")

	outfile.write("\n| [%s](%s) | %s |"%(card.get(name), cardUrl, cardStatusAsText))

def writeCardsToSite(cards, outfile):
	for card in sorted(cards, key=operator.itemgetter('status')):
		writeCardToSite(card,outfile)

def writeHeader(outfile):
	outfile.write("---\ntitle:  \"Common Charity++\"\n---")
	outfile.write("\n\n## Common Charity++ F&L list\n\n")
	outfile.write("Please note if a card is not here, it is subject to normal Common Charity legality\n\n")
	outfile.write("[You can find the EDOPRO banlist here](https://github.com/diamonddudetcg/edopro-custom-banlists/raw/main/banlist/cc%2B%2B.lflist.conf)\n\n")
	outfile.write("\n\n| Card name | Status |")
	outfile.write("\n| :-- | :-- |")

def writeFooter(outfile):
	outfile.write("\n\n###### [Back home](index)")

def printSite():
	with open(siteFilename, 'w', encoding="'utf-8") as siteFile:
		writeHeader(siteFile)
		writeCardsToSite(siteCards, siteFile)
		writeFooter(siteFile)

def printBanlist():
	with open(banlistFilename, 'w', encoding="utf-8") as outfile:
		outfile.write("#[CC++ Format]\n")
		outfile.write("!CC++ %s.%s\n\n" % (datetime.now().month, datetime.now().year))
		outfile.write("\n#OCG Cards\n\n")
		for card in ocgCards:
			writeCardToBanlist(card, outfile)
		outfile.write("\n#Regular Banlist\n\n")
		for card in simpleCards:
			writeCardToBanlist(card, outfile)

def generateArrays():
	with urllib.request.urlopen(request) as url:
		cards = json.loads(url.read().decode()).get(data)
		for card in cards:
			if card.get(card_sets) != None:
				images = card.get(card_images)
				banInfo = card.get(banlist_info)
				banTcg = 3
				if (banInfo == None):
					banTcg = 3	
				if (banInfo != None):
					banlistStatus = banInfo.get(ban_tcg)
					if (banlistStatus == None):
						banTcg = 3
					if (banlistStatus == banned):
						banTcg = 0
					if (banlistStatus == limited):
						banTcg = 1
					if (banlistStatus == semi):
						banTcg = 2

				cardSets = card.get(card_sets)
				hasCommonPrint = False
				for printing in cardSets:
					if printing.get(rarity_code) in legalRarities:
						hasCommonPrint = True

				if not hasCommonPrint:
					banTcg = -1

				cardName = card.get(name)
				pushToSite = False
				if cardName in additionalForbidden:
					banTcg = 0
					additionalForbidden.remove(cardName)
					pushToSite = True
				if card.get(name) in additionalLimited:
					banTcg = 1
					additionalLimited.remove(cardName)
					pushToSite = True
				if card.get(name) in additionalSemiLimited:
					banTcg = 2
					additionalSemiLimited.remove(cardName)
					pushToSite = True
				if card.get(name) in additionalUnlimited:
					banTcg = 3
					additionalUnlimited.remove(cardName)
					pushToSite = True

				alreadyInSite = False
				for variant in images:
					simpleCard = {}
					simpleCard[name] = card.get(name)
					simpleCard[status] = banTcg
					simpleCard[cardId] = variant.get(cardId)
					if not alreadyInSite:
						if pushToSite:
							siteCards.append(simpleCard)
						alreadyInSite = True
					if (banTcg<3):
						simpleCards.append(simpleCard)

			if (card.get(card_sets)) == None and card.get(cardType) != token:
				for variant in card.get(card_images):
					simpleCard = {}
					simpleCard[name] = card.get(name)
					simpleCard[status] = -1
					variantCardId = variant.get(cardId)
					simpleCard[cardId] = variantCardId
					ocgCards.append(simpleCard)

generateArrays()
printBanlist()
printSite()
printAdditionalArrays()