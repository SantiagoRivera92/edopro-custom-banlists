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
additionalLegalCards = [40740224,49928686,75922381,2311090,1295442,	74078255,37961969,62133026,9238125,61011438,98416533,34800281,1855886,63748694,132308,63526052,99910751,61681816,66569334,93953933,81019803,52553471,42431833,88836438,14220547,13386407,49658464,1041278,38436986,74920585,37313338,63708033,36591747,63086455,35479109,9416697,38082437,64487132,1876841,37260946,90659259,36148308]

#Cards that are listed as legal in YGOPRODECK but aren't
notLegalCards = []

#(C) is common, (SP) is Short Print, (SSP) is Super Short Print
legalRarities = ['(C)', '(SP)', '(SSP)']

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
banlistFilename = 'banlist/charity.lflist.conf'
siteFilename ='site/ccbanlist.md'

#Filenames for traditional banlist file
tradFilename = 'banlist/charity_traditional.lflist.conf'
tradSiteFilename = 'site/tradccbanlist.md'

#Card arrays
siteCards = []
simpleCards = [] # List of all TCG legal cards for banlist generation
ocgCards = [] # List of all OCG exclusive cards for banlist generation.

def printCorrectAdditionalCards():
	if len(additionalLegalCards) == 0:
		print("You can remove the entire Additional array safely\n", flush=True)
	else:
		print("Still missing from YGOPRODECK:\n", flush=True)
		print(additionalLegalCards)

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

def writeCardsToTradSite(cards, outfile):
	for card in cards:
		if card.get(status) == 0:
			card[status] = 1
	writeCardsToSite(cards, outfile)

def writeHeader(outfile):
	outfile.write("---\ntitle:  \"Common Charity\"\n---")
	outfile.write("\n\n## Common Charity F&L list")
	outfile.write("\n\n[You can find the EDOPRO banlist here](https://drive.google.com/file/d/1-1HTHnYJyKyyBg94iAwFm-uNayfp0yyT/view?usp=sharing). Open the link, click on the three dots in the top right and then click Download.")
	outfile.write("\n\nThe banlist file goes into the lflists folder in your EDOPRO installation folder. Assuming you use Windows, it usually is C:/ProjectIgnis/lflists")
	outfile.write("\n\nEDOPRO will not recognize a change in banlists while it is open. You will have to restart EDOPRO for the changes to be reflected.")
	outfile.write("\n\n| Card name | Status |")
	outfile.write("\n| :-- | :-- |")

def writeTradHeader(outfile):
	outfile.write("---\ntitle:  \"Common Charity Traditional\"\n---")
	outfile.write("\n\n## Common Charity Traditional F&L list")
	outfile.write("\n\n[You can find the EDOPRO banlist here](https://drive.google.com/file/d/1-3lOtJxeXHMrY5zpUorZCOpVCi4aO1lU/view?usp=sharing). Open the link, click on the three dots in the top right and then click Download.")
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
	print("Writing traditional site", flush=True)
	with open(tradSiteFilename, 'w', encoding="utf-8") as siteFile:
		writeTradHeader(siteFile)
		writeCardsToTradSite(siteCards, siteFile)
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
	print("Writing traditional EDOPRO banlist", flush=True)
	with open(tradFilename, 'w', encoding="utf-8") as outfile:
		outfile.write("#[Common Charity Traditional Format]\n")
		outfile.write("!Common Charity Traditional %s.%s\n\n" % (datetime.now().month, datetime.now().year))
		outfile.write("\n#OCG Cards\n\n")
		for card in ocgCards:
			writeCardToBanlist(card, outfile)
		outfile.write("\n#Regular Banlist\n\n")
		for card in simpleCards:
			newCard = {}
			newCard[cardId] = card.get(cardId)
			newCard[name] = card.get(name)
			newCard[status] = card.get(status)
			if (newCard.get(status) == 0):
				newCard[status] = 1
			writeCardToBanlist(newCard, outfile)

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

				#Manually add the cards that don't have legal prints but should be legal
				if card.get(cardId) in additionalLegalCards:
					if hasCommonPrint: 
						additionalLegalCards.remove(card.get(cardId))
					if not hasCommonPrint:
						hasCommonPrint = True

				if not hasCommonPrint:
					banTcg = -1

				if card.get(cardId) in notLegalCards:
					banTcg = -1

				alreadyInSite = False
				for variant in images:
					simpleCard = {}
					simpleCard[name] = card.get(name)
					simpleCard[status] = banTcg
					simpleCard[cardId] = variant.get(cardId)
					if not alreadyInSite:
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
					willBeLegal = False
					if variantCardId in additionalLegalCards:
						willBeLegal = True
						simpleCard[status] = 3
					if not willBeLegal:
						ocgCards.append(simpleCard)

					siteCards.append(simpleCard)
generateArrays()
printBanlist()
printSite()
printCorrectAdditionalCards()