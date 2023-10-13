import http.client
import json

apiKey = 'x'
apiHost = 'moviesdatabase.p.rapidapi.com'

connection = http.client.HTTPSConnection(apiHost)
headers = {'X-RapidAPI-Key': apiKey, 'X-RapidAPI-Host': apiHost}

urlBase = '/titles/'
seriesId = 'tt0108778'
fullUrl = urlBase + seriesId

connection.request("GET", fullUrl, headers=headers)
response = connection.getresponse()
data = response.read()

movieInfo = json.loads(data.decode("utf-8"))

print('=========================================')
print('The TV show ' + movieInfo['results']['titleText']['text'] + ' first aired in ' + str(movieInfo['results']['releaseYear']['year']) + ' and ran until ' + str(movieInfo['results']['releaseYear']['endYear']) + '.')

