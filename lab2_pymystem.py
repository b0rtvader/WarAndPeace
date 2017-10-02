from pymystem3 import Mystem
geoset=set()
t = Mystem()
f=open("warANDpeaceSmall.txt", "rb")    
for line in f:    
    for i in t.analyze(line.decode('utf8')):        
        if('analysis' in i.keys()):
            if(len(i['analysis'])>0):                
                if('gr' in i['analysis'][0].keys()):                    
                    if('гео' in i['analysis'][0]['gr']):
			geoset.add(i['analysis'][0]['lex'])
  print(geoset)
