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

filename = 'dt_exclusives.md'

name = 'name'
cardId = 'id'
status = 'status'

def writeCard(card, outfile):
	cardUrl = "https://db.ygoprodeck.com/card/?search=%s"%card.get(name).replace(" ", "%20")
	outfile.write("\n[%s](%s)"%(card.get(name), cardUrl))

def writeCards(cards, outfile):
	for card in cards:
		writeCard(card,outfile)

def writeHeader(outfile):
	outfile.write("---\ntitle:  \"Common Charity\"\n---\n")
	outfile.write("### Cards that were only printed in Duel Terminal")

def writeFooter(outfile):
	outfile.write("\n###### [Back home](index)")

with urllib.request.urlopen(request) as url:
	with open(filename, 'w', encoding="utf-8") as outfile:
		cards = json.loads(url.read().decode()).get('data')
		simpleCards = []
		for card in cards:
			if card.get('card_sets') != None:
				cardSets = card.get('card_sets')
				hasCommonPrint = False
				isDT = False
				for printing in cardSets:
					rarity = printing.get('set_rarity_code')
					if rarity == '(C)' or rarity == '(SP)' or rarity == '(SSP)':
						hasCommonPrint = True
					elif rarity == '(DNPR)':
						isDT = True
				if isDT:
					if not hasCommonPrint:
						simpleCard = {}
						simpleCard[name] = card.get(name)
						simpleCard[cardId] = card.get(cardId)
						simpleCards.append(simpleCard)
		writeHeader(outfile)
		writeCards(simpleCards, outfile)
		writeFooter(outfile)