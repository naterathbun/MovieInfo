import http.client
import json

apiKey = ''
apiHost = 'moviesdatabase.p.rapidapi.com'

connection = http.client.HTTPSConnection(apiHost)
headers = {'X-RapidAPI-Key': apiKey, 'X-RapidAPI-Host': apiHost}

urlBase = '/titles/series/'
seriesId = 'tt0108778'
fullUrl = urlBase + seriesId

connection.request("GET", fullUrl, headers=headers)
response = connection.getresponse()
data = response.read()

movieInfo = json.loads(data.decode("utf-8"))

print('=========================================')


