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

#Cards that aren't in YGOPRODECK but are legal. As of right now, it's only Ghost Ogre
temporarilyLegalCards = [59438930]

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
filename = 'charity.lflist.conf'

def writeCard(card, outfile):
	outfile.write("%d %d -- %s\n" % (card.get(cardId), card.get(status), card.get(name)))

with urllib.request.urlopen(request) as url:
	cards = json.loads(url.read().decode()).get(data)
	simpleCards = []
	ocgCards = []
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
			if not hasCommonPrint:
				if card.get(cardId) in temporarilyLegalCards:
					hasCommonPrint = True

			if not hasCommonPrint:
				banTcg = -1

			if (banTcg<3):
				for variant in images:
					simpleCard = {}
					simpleCard[name] = card.get(name)
					simpleCard[status] = banTcg
					simpleCard[cardId] = variant.get(cardId)
					simpleCards.append(simpleCard)
		if (card.get(card_sets)) == None and card.get(cardType) != token:
			simpleCard = {}
			simpleCard[name] = card.get(name)
			simpleCard[status] = -1
			for variant in card.get(card_images):
				simpleCard[cardId] = variant.get(cardId)
				ocgCards.append(simpleCard)
	with open(filename, 'w', encoding="utf-8") as outfile:
		outfile.write("#[Common Charity Format]\n")
		outfile.write("!Common Charity %s.%s\n\n" % (datetime.now().month, datetime.now().year))
		outfile.write("\n#OCG Cards\n\n")
		for card in ocgCards:
			writeCard(card, outfile)
		outfile.write("\n#Regular Banlist\n\n")
		for card in simpleCards:
			writeCard(card, outfile)