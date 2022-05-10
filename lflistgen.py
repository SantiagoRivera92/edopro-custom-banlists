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

#Cards that aren't in YGOPRODECK but are legal. 
temporarilyLegalCards = []

#Cards that aren't released yet but are confirmed as commons.
futureLegalCards = [84332527,21727231,57111330,83488497,19882096,46877100,18760514,45154513,71549257,18548966,44932065,70427670,17825378,43210483,70204022,79582540,5577149,52253888,32975247,78360952,4754691,31259606,67248304,4632019,30037118,66309175,24070330,23848752,96637156,83670388,10065487,82735249,45115956,81613061,17008760,44092304,70491413,17885118,79775821,42158279,5941982,32335697,4825390,31213049,7608148,101108081,101108084,101108085,64806765,13536606]

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
filename = 'banlist/charity.lflist.conf'

def writeCard(card, outfile):
	try:
		outfile.write("%d %d -- %s\n" % (card.get(cardId), card.get(status), card.get(name)))
	except TypeError:
		print(card)

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
				variantCardId = variant.get(cardId)
				willBeLegal = False
				for futureCardId in futureLegalCards:
					if futureCardId == variantCardId:
						willBeLegal = True
				if not willBeLegal:
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