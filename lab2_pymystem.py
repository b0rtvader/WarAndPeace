from pymystem3 import Mystem
mystem = Mystem()
with open("warANDpeace.txt", "rb") as f: 
    sourceText = f.read().decode('utf8')   
for token in mystem.analyze(sourceText): 
    try:       
        for tokenAnalysis in token['analysis']:
            if('гео' in tokenAnalysis['gr']):
                print(tokenAnalysis['lex'])
    except KeyError:        # Возникает в спецсимволах. (token['analysis'] отсутствует)
    	pass
