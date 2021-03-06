import re
import pymorphy2

with open("warANDpeace.txt", "rb") as f: 
	sourceText = f.read().decode('utf8')

MISTRUTH_DEGREE = 0.4 # степень недоверия библиотеке pymorphy2 :)

geoSet = set()
words = re.findall(r'[ёа-яА-Я-]{3,}', sourceText)

morph = pymorphy2.MorphAnalyzer()

for word in words:
	parse = morph.parse(word)
	for p in parse:
		if ('Geox' in p.tag) and (p.score > MISTRUTH_DEGREE):
			geoSet.add(p.normal_form)
for geo in sorted(geoSet):
	print(geo)
