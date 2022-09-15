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


#Banlist status
banned = 'Banned'
limited = 'Limited'
semi = 'Semi-Limited'

#YGOPRODECK API keys
data = 'data'
card_sets = 'card_sets'
banlist_info = 'banlist_info'
ban_tcg = 'ban_tcg'
set_code = 'set_code'
card_images = 'card_images'
cardType = 'type'

#Token stuff
token = 'Token'

#My keys
name = 'name'
cardId = 'id'
status = 'status'

formatName = "DREV"

#Filenames for banlist file
banlistFilename = 'banlist/wmy/wmy_%s.lflist.conf'%formatName


#Arrays for sets
unlimitedSets = ["DREV-"]
semiLimitedSets = ["TSHD-", "STBL-", "SDMM-", "5DS3-", "SDMA-"]
limitedSets = ["ABPF-", "STOR-", "DPKB-", "DT02-", "GLD3-", "TU03-", "HA02-", "WCPP-", "DT03-", "TU04-", "DL11-", "HA03", "DP10", "DT04"]
additionalLimitedCards = [
	"Cyber Eltanin",
	"Synchro Blast Wave",
	"Speed Warrior",
	"Advance Draw",
	"Scrap-Iron Scarecrow",
	"Level Eater",
	"One for One",
	"Dandylion",
	"Angel 07",
	"Hundred Eyes Dragon",
	"Darklord Asmodeus",
	"Darklord Superbia",
	"Darklord Edeh Arae",
	"Alector, Sovereign of Birds",
	"Golem Dragon",
	"Van'Dalgyon the Dark Dragon Lord",
	"Cyber Dinosaur",
	"Green Baboon, Defender of the Forest",
	"The Wicked Eraser",
	"Blackwing - Vayu the Emblem of Honor",
	"Chimeratech Fortress Dragon",
	"Archfiend of Gilfer",
	"The Wicked Dreadroot",
	"Dark Armed Dragon",
	"Dragonic Knight",
	"Malefic Stardust Dragon",
	"Gold Sarcophagus",
	"Blue-Eyes White Dragon",
	"Dark Magician",
	"Red-Eyes Black Dragon",
	"Darklord Desire",
	"Dark End Dragon",
	"Elemental HERO Ocean",
	"Dreadscythe Harvester",
	"Gandora the Dragon of Destruction",
	"Magician's Valkyria",
	"The Wicked Avatar",
	"Exodius the Ultimate Forbidden Lord",
	"Red Dragon Archfiend",
	"XX-Saber Fullhelmknight",
	"The Winged Dragon of Ra"
	
]


simpleCards = [] # List of all TCG legal cards for banlist generation


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

def printBanlist():
	print("Writing default EDOPRO banlist", flush=True)
	with open(banlistFilename, 'w', encoding="utf-8") as outfile:
		outfile.write("#[Wave Motion Yugioh %s]\n" % formatName)
		outfile.write("!Wave Motion Yugioh %s\n\n" % formatName)
		outfile.write("#whitelist\n\n")
		for card in simpleCards:
			writeCardToBanlist(card, outfile)

def generateArrays():
	with urllib.request.urlopen(request) as url:
		cards = json.loads(url.read().decode()).get(data)
		for card in cards:
			if card.get(card_sets) != None:
				images = card.get(card_images)
				banInfo = card.get(banlist_info)
				banTcg = -1

				cardSets = card.get(card_sets)
				hasCommonPrint = False
				if card.get(name) in additionalLimitedCards:
					banTcg = 1
				for printing in cardSets:
					for setCode in limitedSets:
						if printing.get(set_code).startswith(setCode):
							banTcg = 1
				for printing in cardSets:
					for setCode in semiLimitedSets:
						if printing.get(set_code).startswith(setCode):
							banTcg = 2
				for printing in cardSets:
					for setCode in unlimitedSets:
						if printing.get(set_code).startswith(setCode):
							banTcg = 3

				for variant in images:
					if (banTcg<3):
						simpleCard = {}
						simpleCard[name] = card.get(name)
						simpleCard[status] = banTcg
						simpleCard[cardId] = variant.get(cardId)
						simpleCards.append(simpleCard)

			if (card.get(card_sets)) == None and card.get(cardType) != token:
				for variant in card.get(card_images):
					simpleCard = {}
					simpleCard[name] = card.get(name)
					simpleCard[status] = -1
					variantCardId = variant.get(cardId)
					simpleCard[cardId] = variantCardId
					simpleCards.append(simpleCard)

generateArrays()
printBanlist()