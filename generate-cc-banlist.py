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
#This is a temporary fix until YGOPRODECK includes portuguese commons for OP15, OP16 and OP17 specifically
portugueseOTSLegalCards = [98259197,40391316,24040093,98024118,19439119,10118318,47395382,29905795,66976526,60470713,76442347,36318200,15941690,88552992,4192696,2461031,16550875,69207766,90576781,21179143,64514622,3300267,31516413,78033100,41639001,13140300,8611007,51555725,38492752,32761286]
with urllib.request.urlopen(request) as url:
		cards = json.loads(url.read().decode()).get('data')
		simpleCards = []
		ocgCards = []
		for card in cards:
			if card.get('card_sets') != None:
				simpleCard = {}
				simpleCard['name'] = card.get('name')
				simpleCard['id'] = card.get('id')
				banlistInfo = card.get('banlist_info')
				banTcg = 3
				if (banlistInfo == None):
					banTcg = 3	
				if (banlistInfo != None):
					status = banlistInfo.get('ban_tcg')
					if (status == None):
						banTcg = 3
					if (status == 'Banned'):
						banTcg = 0
					if (status == 'Limited'):
						banTcg = 1
					if (status == 'Semi-Limited'):
						banTcg = 2

				cardSets = card.get('card_sets')
				hasCommonPrint = False

				for printing in cardSets:
					rarity = printing.get('set_rarity_code')
					if rarity == '(C)' or rarity == '(SP)' or rarity == '(SSP)':
						hasCommonPrint = True

				#Portuguese fix, remove as soon as YGOPRODECK adds portuguese OTS support
				if not hasCommonPrint:
					for cardId in portugueseOTSLegalCards:
						if card.get('id') == cardId:
							hasCommonPrint = True

				if not hasCommonPrint:
					banTcg = -1

				if (banTcg<3):
					simpleCard['status'] = banTcg
					simpleCards.append(simpleCard)
			if (card.get('card_sets')) == None:
				simpleCard = {}
				simpleCard['name'] = card.get('name')
				simpleCard['id'] = card.get('id')
				simpleCard['status'] = -1
				ocgCards.append(simpleCard)
		specialCases = [
			{'name':'Monster Reborn', 'id':83764718, 'status':1}
		]
		with open('charity.lflist.conf', 'w', encoding="utf-8") as outfile:
			outfile.write("#[Common Charity Format]\n")
			outfile.write("!Common Charity %s.%s\n\n" % (datetime.now().month, datetime.now().year))
			outfile.write("#Special Cases\n\n")
			for card in specialCases:
				outfile.write("%d %d -- %s\n" % (card.get('id'), card.get('status'), card.get('name')))
			outfile.write("\n#OCG Cards\n\n")
			for card in ocgCards:
				outfile.write("%d %d -- %s\n" % (card.get('id'), card.get('status'), card.get('name')))
			outfile.write("\n#Regular Banlist\n\n")
			for card in simpleCards:
				outfile.write("%d %d -- %s\n" % (card.get('id'), card.get('status'), card.get('name')))