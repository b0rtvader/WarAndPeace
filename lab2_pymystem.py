import re
from pymystem3 import Mystem

with open("warANDpeaceSmall.txt", "rb") as f: 
	sourceText = f.read().decode('utf8')

words = re.findall(r'[ёа-яА-Я-]{3,}', sourceText)
mystem = Mystem()
geoSet = set()

for word in words:
	analysis = mystem.analyze(word)[0].get('analysis')		# метод analyze() возвращает список из 2 элементов: 1. разбор самого слова, 2. разбор символа '\n' (откуда берется '\n' ??)

	gr = analysis[0].get('gr')								# значение по ключу 'analysis' содержит список из одного элемента, в котором словарь с ключами 'gr' и 'lex')
	normalForm = analysis[0].get('lex')
	if 'гео' in gr:
		geoSet.add(normalForm)

print(geoSet)
