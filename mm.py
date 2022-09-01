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
	"A.I. Contact", 
	"Amazoness Archer", 
	"Amorphactor Pain, the Imagination Dracoverlord", 
	"Anti-Spell Fragrance",
	"Barrier Statue of the Abyss",
	"Barrier Statue of the Drought",
	"Barrier Statue of the Heavens",
	"Barrier Statue of the Inferno",
	"Barrier Statue of the Stormwinds",
	"Barrier Statue of the Torrent",
	"Beast of the Pharaoh",
	"Card of Demise",
	"Contact \"C\"",
	"Contract with Don Thousand",
	"Crystron Halqifibrax",
	"Cannon Soldier",
	"Cannon Soldier MK-II",
	"Dimensional Barrier",
	"Dinomist Spinos",
	"El-Shaddoll Winda",
	"Fallen of Albaz",
	"Floowandereeze and the Magnificent Map",
	"Fossil Dyna Pachycephalo",
	"Geomathmech Final Sigma",
	"Gigantic Spright",
	"Gozen Match",
	"Inspector Boarder",
	"Luna Light Perfume",
	"Masked HERO Dark Law",
	"Megalith Bethor",
	"Megalith Phul",
	"Mystic Mine",
	"Necrovalley",
	"Number 39: Utopia Beyond",
	"Number 41: Bagooska the Terribly Tired Tapir",
	"Phantasmal Lord Ultimitl Bishbaalkin",
	"Primal Seed",
	"Raiza the Mega Monarch",
	"Reprodocus",
	"Right-Hand Shark"
	"Rivalry of Warlords",
	"Secret Village of the Spellcasters",
	"Skill Drain",
	"Tenyi Spirit - Ashuna",
	"The Monarchs Erupt",
	"There Can Be Only One",
	"Time Thief Redoer",
	"Toon Cannon Soldier",
	"Virtual World Kyubi - Shenshen"
]

additionalLimited = [
	"Adamancipator Friends",
	"Cyber Angel Benten",
	"Cyber Emergency",
	"Darklord Nurse Reficule",
	"Denko Sekka",
	"Dinomist Charge",
	"Drytron Alpha Thuban",
	"F.A. Hang On Mach",
	"Fossil Dig",
	"Heavenly Dragon Circle",
	"Limiter Removal",
	"Morphtronic Telefon",
	"M-X Saber Invoker",
	"Number 42: Galaxy Tomahawk",
	"Personal Spoofing",
	"Predapractice",
	"Twin Twisters"
]

additionalSemiLimited = [
	"Altergeist Multifaker",
	"Cyber Dragon",
	"Pot of Duality",
	"Predaplant Triantis",
	"Speedroid Taketomborg"	
]
additionalUnlimited = []


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

#Filenames for banlist file
banlistFilename = 'banlist/mm/market_masters.lflist.conf'

#Card arrays
siteCards = []
simpleCards = [] # List of all TCG legal cards for banlist generation
ocgCards = [] # List of all OCG exclusive cards for banlist generation.


def writeCardToBanlist(card, outfile):
	try:
		outfile.write("%d %d -- %s\n" % (card.get(cardId), card.get(status), card.get(name)))
	except TypeError:
		print(card)

def printBanlist():
	print("Writing default EDOPRO banlist", flush=True)
	with open(banlistFilename, 'w', encoding="utf-8") as outfile:
		outfile.write("#[Market Masters]\n")
		outfile.write("!Market Masters %s.%s\n\n" % (datetime.now().month, datetime.now().year))
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

				if card.get(name) in additionalForbidden:
					banTcg = 0
				if card.get(name) in additionalLimited:
					banTcg = 1
				if card.get(name) in additionalSemiLimited:
					banTcg = 2
				if card.get(name) in additionalUnlimited:
					banTcg = 3

				if (banTcg < 3):
					for variant in images:
						simpleCard = {}
						simpleCard[name] = card.get(name)
						simpleCard[status] = banTcg
						simpleCard[cardId] = variant.get(cardId)
						simpleCards.append(simpleCard)



generateArrays()
printBanlist()