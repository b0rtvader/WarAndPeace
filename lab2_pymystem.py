from pymystem3 import Mystem
geoset=set()
mystem = Mystem()
with open("warANDpeaceSmall.txt", "rb") as f: 
    sourceText = f.read().decode('utf8')   
for token in mystem.analyze(sourceText):        
    if('analysis' in token.keys()):
        tokenAnalysis = token['analysis']
        if(len(tokenAnalysis)>0) and ('гео' in tokenAnalysis[0]['gr']):
            geoset.add(tokenAnalysis[0]['lex'])
print(geoset)
