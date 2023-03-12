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

#Cards that aren't in YGOPRODECK but are legal. 
additionalLegalCards = [44179224, 60222582, 46159582, 34968834, 54757758, 84640866, 2055403, 75902998, 3072808,67111213,93506862,39905966,92784374,37557626,36227804
,11877465, 57272170, 21496848, 45222299, 28429121, 46337945]
newAdditionalLegalcards = []

#Cards that are listed as legal in YGOPRODECK but aren't
notLegalCards = [88926295, 1011091, 51522296, 35569555, 85969517]
stillWrong = []

#(C) is common, (SP) is Short Print, (SSP) is Super Short Print
legalRarities = ['(C)', '(SP)', '(SSP)']

#Banlist status
banned = 'Banned'
limited = 'Limited'
semi = 'Semi-Limited'

#References for the redesign

VANILLA_REF = "<img src=\"assets/vanilla.png\" alt=\"Normal Monster\" width=\"12\" height=\"12\"/>"
EFFECT_REF = "<img src=\"assets/effect.png\" alt=\"Effect Monster\" width=\"12\" height=\"12\"/>"
RITUAL_REF = "<img src=\"assets/ritual.png\" alt=\"Ritual Monster\" width=\"12\" height=\"12\"/>"
FUSION_REF = "<img src=\"assets/fusion.png\" alt=\"XYZ Fusion\" width=\"12\" height=\"12\"/>"
LINK_REF = "<img src=\"assets/link.png\" alt=\"Link Monster\" width=\"12\" height=\"12\"/>"
SYNCHRO_REF = "<img src=\"assets/synchro.png\" alt=\"Synchro Monster\" width=\"12\" height=\"12\"/>"
XYZ_REF = "<img src=\"assets/xyz.png\" alt=\"XYZ Monster\" width=\"12\" height=\"12\"/>"
SPELL_REF = "<img src=\"assets/spell.png\" alt=\"Spell\" width=\"12\" height=\"12\"/>"
TRAP_REF = "<img src=\"assets/trap.png\" alt=\"Trap\" width=\"12\" height=\"12\"/>"
OTHER_REF = "<img src=\"assets/other.png\" alt=\"Trap\" width=\"12\" height=\"12\"/>"

CARD_TYPE_NORMAL_MONSTER = 1
CARD_TYPE_EFFECT_MONSTER = 2
CARD_TYPE_RITUAL_MONSTER = 3
CARD_TYPE_FUSION_MONSTER = 4
CARD_TYPE_LINK_MONSTER = 5
CARD_TYPE_SYNCHRO_MONSTER = 6
CARD_TYPE_XYZ_MONSTER = 7
CARD_TYPE_SPELL = 98
CARD_TYPE_TRAP = 99
CARD_TYPE_OTHER = 0

CARD_TYPE_KEY = "internal_card_type"

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
skill = 'Skill Card'

#My keys
name = 'name'
cardId = 'id'
status = 'status'

#Filenames for banlist file
banlistFilename = 'banlist/charity.lflist.conf'
tradFilename = "banlist/charity_trad.lflist.conf"
siteFilename ='site/ccbanlist.md'

#Card arrays
siteCards = []
simpleCards = [] # List of all TCG legal cards for banlist generation
ocgCards = [] # List of all OCG exclusive cards for banlist generation.

def printCorrectAdditionalCards():
	if len(newAdditionalLegalcards) == 0:
		print("You can remove the entire Additional array safely\n", flush=True)
	else:
		print("Still missing from YGOPRODECK:\n", flush=True)
		print(newAdditionalLegalcards, flush=True)
	if len(stillWrong) == 0:
		print("You can remove the entire notlegalcards array safely\n", flush=True)
	else:
		print("Still wrong:\n", flush=True)
		print(stillWrong)

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

	img = getImageRefStringFromInteger(card[CARD_TYPE_KEY])

	cardUrl = "https://db.ygoprodeck.com/card/?search=%s"%card.get(name).replace(" ", "%20").replace("&", "%26")

	outfile.write("\n|%s [%s](%s) | %s |"%(img, card.get(name), cardUrl, cardStatusAsText))

def writeCardsToSite(cards, outfile):
	for card in cards:
		if card[CARD_TYPE_KEY] == None:
			print(card['name'])
	for card in sorted(cards, key=operator.itemgetter('status', CARD_TYPE_KEY)):
		writeCardToSite(card,outfile)


def writeHeader(outfile):
	outfile.write("---\ntitle:  \"Common Charity\"\n---")
	outfile.write("\n\n## Common Charity F&L list")
	outfile.write("\n\n[You can find the EDOPRO banlist here](https://drive.google.com/file/d/1-1HTHnYJyKyyBg94iAwFm-uNayfp0yyT/view?usp=sharing). Open the link, click on the three dots in the top right and then click Download.")
	outfile.write("\n\nThe banlist file goes into the lflists folder in your EDOPRO installation folder. Assuming you use Windows, it usually is C:/ProjectIgnis/lflists")
	outfile.write("\n\nEDOPRO will not recognize a change in banlists while it is open. You will have to restart EDOPRO for the changes to be reflected.")
	outfile.write("\n\n| Card name | Status |")
	outfile.write("\n| :-- | :-- |")

def writeFooter(outfile):
	outfile.write("\n\n###### [Back home](index)")

def printSite():
	print("Writing default site", flush=True)
	with open(siteFilename, 'w', encoding="'utf-8") as siteFile:
		writeHeader(siteFile)
		writeCardsToSite(siteCards, siteFile)
		writeFooter(siteFile)

def printBanlist():
	print("Writing default EDOPRO banlist", flush=True)
	with open(banlistFilename, 'w', encoding="utf-8") as outfile:
		outfile.write("#[Common Charity Format]\n")
		outfile.write("!Common Charity %s.%s\n\n" % (datetime.now().month, datetime.now().year))
		outfile.write("\n#OCG Cards\n\n")
		for card in ocgCards:
			writeCardToBanlist(card, outfile)
		outfile.write("\n#Regular Banlist\n\n")
		for card in simpleCards:
			writeCardToBanlist(card, outfile)
		for card in additionalLegalCards:
			outfile.write("%d 3 -- New card\n"%(card))

def printTradBanlist():
	print("Writing trad EDOPRO banlist", flush=True)
	with open(tradFilename, 'w', encoding="utf-8") as outfile:
		outfile.write("#[Common Charity Traditional Format]\n")
		outfile.write("!Common Charity %s.%s (Traditional)\n\n" % (datetime.now().month, datetime.now().year))
		outfile.write("\n#OCG Cards\n\n")
		for card in ocgCards:
			writeCardToBanlist(card, outfile)
		outfile.write("\n#Trad Banlist\n\n")
		for card in simpleCards:
			if card.get(status) != 0:
				writeCardToBanlist(card, outfile)
			if card.get(status) == 0:
				newCard = {}
				newCard[status] = 1
				newCard[cardId] = card.get(cardId)
				newCard[name] = card.get(name)
				writeCardToBanlist(newCard, outfile)
		for card in additionalLegalCards:
			outfile.write("%d 3 -- New card\n"%(card))

def generateArrays():
	with urllib.request.urlopen(request) as url:
		cards = json.loads(url.read().decode()).get(data)
		for card in cards:
			if card.get('type') != token and card.get('type') != skill:
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

					cardTypeAsInt = getCardTypeAsInteger(card)

					cardSets = card.get(card_sets)
					hasCommonPrint = False
					for printing in cardSets:
						if printing.get(rarity_code) in legalRarities:
							hasCommonPrint = True

					#Manually add the cards that don't have legal prints but should be legal
					if card.get(cardId) in additionalLegalCards:
						additionalLegalCards.remove(card.get(cardId))
						if hasCommonPrint: 
							newAdditionalLegalcards.append(card.get(cardId))
						if not hasCommonPrint:
							hasCommonPrint = True

					if card.get(cardId) in notLegalCards:
						if hasCommonPrint:
							stillWrong.append(card.get(cardId))
						hasCommonPrint = False
					
					if not hasCommonPrint:
						banTcg = -1

					alreadyInSite = False
					for variant in images:
						simpleCard = {}
						simpleCard[name] = card.get(name)
						simpleCard[status] = banTcg
						simpleCard[cardId] = variant.get(cardId)
						simpleCard[CARD_TYPE_KEY] = cardTypeAsInt
						if not alreadyInSite:
							siteCards.append(simpleCard)
							alreadyInSite = True
						simpleCards.append(simpleCard)

				else:
					cardTypeAsInt = getCardTypeAsInteger(card)
					for variant in card.get(card_images):
						simpleCard = {}
						simpleCard[name] = card.get(name)
						simpleCard[status] = -1
						variantCardId = variant.get(cardId)
						simpleCard[cardId] = variantCardId
						simpleCard[CARD_TYPE_KEY] = cardTypeAsInt
						willBeLegal = False
						if variantCardId in additionalLegalCards:
							willBeLegal = True
							simpleCard[status] = 3
						if not willBeLegal:
							ocgCards.append(simpleCard)

						siteCards.append(simpleCard)

def getImageRefStringFromInteger(cType):
	if cType == CARD_TYPE_NORMAL_MONSTER:
		return VANILLA_REF
	if cType == CARD_TYPE_EFFECT_MONSTER:
		return EFFECT_REF
	if cType == CARD_TYPE_RITUAL_MONSTER:
		return RITUAL_REF
	if cType == CARD_TYPE_FUSION_MONSTER:
		return FUSION_REF
	if cType == CARD_TYPE_LINK_MONSTER:
		return LINK_REF
	if cType == CARD_TYPE_SYNCHRO_MONSTER:
		return SYNCHRO_REF
	if cType == CARD_TYPE_XYZ_MONSTER:
		return XYZ_REF
	if cType == CARD_TYPE_SPELL:
		return SPELL_REF
	if cType == CARD_TYPE_TRAP:
		return TRAP_REF
	if cType == CARD_TYPE_OTHER:
		return OTHER_REF

def getCardTypeAsInteger(card):
	cType = card.get('type')
	if ("Monster" in cType):
		if "XYZ" in cType:
			return CARD_TYPE_XYZ_MONSTER
		elif "Synchro" in cType:
			return CARD_TYPE_SYNCHRO_MONSTER
		elif "Fusion" in cType:
			return CARD_TYPE_FUSION_MONSTER
		elif "Normal" in cType:
			return CARD_TYPE_NORMAL_MONSTER
		elif "Link" in cType:
			return CARD_TYPE_LINK_MONSTER
		elif "Ritual" in cType:
			return CARD_TYPE_RITUAL_MONSTER
		else:
			return CARD_TYPE_EFFECT_MONSTER
	elif ("Spell" in cType):
		return CARD_TYPE_SPELL
	elif ("Trap" in cType):
		return CARD_TYPE_TRAP
	return CARD_TYPE_OTHER

generateArrays()
printBanlist()
printTradBanlist()
printSite()
printCorrectAdditionalCards()