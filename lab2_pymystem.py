from pymystem3 import Mystem
geoset=set()
mystem = Mystem()
with open("warANDpeace.txt", "rb") as f: 
    sourceText = f.read().decode('utf8')   
for token in mystem.analyze(sourceText): 
    try:       
        tokenAnalysis = token['analysis'][0]
        if('гео' in tokenAnalysis['gr']):
            geoset.add(tokenAnalysis['lex'])
    except KeyError:        # Возникает в спецсимволах. (token['analysis'] отсутствует)
    	pass
    except IndexError:		# Возникает в словах на латинице. Разбор данных слов не проводится (token['analysis'][0] отсутствует)
    	pass
print(sorted(geoset))
