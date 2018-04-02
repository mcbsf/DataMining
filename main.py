import urllib.request, json 
import pandas as pd
from analyser import SentimentAnalyser

#pega a o json dentro da url e bota todos os tópicos mais populares dentro da variável "data"
# with urllib.request.urlopen("http://reddit.com/r/Bitcoin/.json") as url:
#     data = json.loads(url.read())['data']['children']


# with open('data.txt', 'w') as outfile:  
#     json.dump(data, outfile)
'''
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
'''
df = pd.read_csv('csv/comments_data', sep='\t')

emotions = []
for x in df['comment']:
	analyser = SentimentAnalyser()
	dic_emotion = analyser.analyseSentence(x)
	str_emotion = ""
	positive = 0
	negative = 0

	for (emotion, value) in dic_emotion.items():
		print(emotion)
		
		if emotion in 'positive-emotion':
			positive = value

		elif emotion in "negative-emotion":
			negative = value

	emotion_value = str(positive - negative)
	print(emotion_value)
	emotions.append(emotion_value)
	
	
df['comment'] = emotions
df.to_csv("csv/comments_data_and_sentiments.csv", sep='\t', encoding='utf-8')





comment_table = []
