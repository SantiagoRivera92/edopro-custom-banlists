import urllib.request, json 
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

#Filename for banlist
filename = 'ccbanlist.md'

def writeCard(card, outfile):
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

def writeCards(cards, outfile):
	for card in cards:
		writeCard(card,outfile)

def writeHeader(outfile):
	outfile.write("---\ntitle:  \"Common Charity\"\n---")

def writeFooter(outfile):
	outfile.write("\n\n###### [Back home](index)")


illegalCards = []
bannedCards = []
limitedCards = []
semiLimitedCards = []
unlimitedCards = []

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

			simpleCard = {}
			simpleCard[name] = card.get(name)
			simpleCard[cardId] = card.get(cardId)
			simpleCard[status] = banTcg
			if banTcg == -1:
				illegalCards.append(simpleCard)
			elif banTcg == 0:
				bannedCards.append(simpleCard)
			elif banTcg == 1:
				limitedCards.append(simpleCard)
			elif banTcg == 2:
				semiLimitedCards.append(simpleCard)
			elif banTcg == 3:
				unlimitedCards.append(simpleCard)

with open(filename, 'w', encoding="utf-8") as outfile:
	writeHeader(outfile)
	writeCards(illegalCards, outfile)
	writeCards(bannedCards, outfile)
	writeCards(limitedCards, outfile)
	writeCards(semiLimitedCards, outfile)
	writeCards(unlimitedCards, outfile)
	writeFooter(outfile)