import urllib.request, json 

#pega a o json dentro da url e bota todos os tópicos mais populares dentro da variável "data"
with urllib.request.urlopen("http://reddit.com/r/Bitcoin/.json") as url:
    data = json.loads(url.read())['data']['children']

urls = []
#pega a url de acesso aos tópicos
for topic in data:
	urls.append(topic["data"]["url"])

for url in urls:
	print(url)