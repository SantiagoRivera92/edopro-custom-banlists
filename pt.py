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

filename = "site/pt_exclusives.md"

def writeCard(card, outfile):
	cardUrl = "https://db.ygoprodeck.com/card/?search=%s"%card.get('name').replace(" ", "%20")
	outfile.write("\n| [%s](%s) | %s |"%(card.get('name'), cardUrl, card.get('set')))

def writeCards(cards, outfile):
	for card in cards:
		writeCard(card,outfile)

def writeHeader(outfile):
	outfile.write("---\ntitle:  \"Common Charity\"\n---")
	outfile.write("\n\n## Portuguese OTS exclusives")
	outfile.write("\n| Card name | Set |")
	outfile.write("\n| :-- | :-- |")

def writeFooter(outfile):
	outfile.write("\n\n###### [Back home](index)")

with urllib.request.urlopen(request) as url:
	cards = json.loads(url.read().decode()).get('data')
	portugueseOTSCards = []
	for card in cards:
		if card.get('card_sets') != None:
			cardSets = card.get('card_sets')
			hasCommonPrint = False
			isPortuguese = False
			printSet = ""
			for printing in cardSets:
				rarity = printing.get('set_rarity_code')
				if rarity == '(C)':
					if '(POR)' in printing.get('set_name'):
						isPortuguese = True
						printSet = printing.get('set_code')
					else:
						hasCommonPrint = True

			if isPortuguese:
				if not hasCommonPrint:
					simpleCard = {}
					simpleCard['name'] = card.get('name')
					simpleCard['id'] = card.get('id')
					simpleCard['set'] = printSet
					portugueseOTSCards.append(simpleCard)

	with open(filename, 'w', encoding="utf-8") as outfile:
		writeHeader(outfile)
		writeCards(portugueseOTSCards, outfile)
		writeFooter(outfile)