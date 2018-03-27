import urllib.request, json 
from analyser import SentimentAnalyser

#pega a o json dentro da url e bota todos os tópicos mais populares dentro da variável "data"
# with urllib.request.urlopen("http://reddit.com/r/Bitcoin/.json") as url:
#     data = json.loads(url.read())['data']['children']


# with open('data.txt', 'w') as outfile:  
#     json.dump(data, outfile)

urls = []
topics_id = []
counter = 0

with open('data.txt') as json_file:  
    data = json.load(json_file)

#pega a url de acesso aos tópicos
for topic in data:
	urls.append("http://reddit.com"+topic["data"]["permalink"])
	topics_id.append(topic["data"]["id"])

for url in urls:
	print(url)
	print(topics_id[counter])
	counter = counter + 1
	
#INÍCIO DO CÒDIGO PARA COMEÇAR A MONTAR A TABELA DE COMENTÁRIOS	
	# with urllib.request.urlopen(url) as url_aux:
 #    	data = json.loads(url_aux.read())['data']['children']
    	
 #    	with open('comment_table.txt', 'w') as outfile:  
	#     	json.dump(data, outfile)	

analyser = SentimentAnalyser()
print(analyser.analyseSentence('hate hate, love happy none'))

comment_table = []

