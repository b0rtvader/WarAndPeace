import re
import pymorphy2

with open("warANDpeace.txt", "rb") as f: 
	wordList = f.read().decode('utf8')

MISTRUTH_DEGREE = 0.5 # степень недоверия библиотеке pymorphy2 :)

# регулярка выбирает такие слова, например: Москва, Москва-река, Франкфурт-на-Майне
# географических названий более чем с двумя дефисами, наверное, нет)
words = re.findall(r'\w{3,100}|\w+\-\w+|\w+\-\w+\-\w+', wordList)

morph = pymorphy2.MorphAnalyzer()
geoSet = set()

for word in words:
	parse = morph.parse(word)
	for p in parse:
		if ('Geox' in p.tag) and (p.score > MISTRUTH_DEGREE):
			geoSet.add(p.normal_form)
print(geoSet)
