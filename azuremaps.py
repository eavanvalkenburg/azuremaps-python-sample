import requests
import json

config_file = 'config.json'

key = json.load(open(config_file))['key']
travel_mode = 'car'

routeUrl  = 'https://atlas.microsoft.com/route/directions/json'
matrixUrl  = 'https://atlas.microsoft.com/route/matrix/json'

loc1 = [52.303754, 4.750214]
loc2 = [52.357430, 4.927950]
query = f'{loc1[0]},{loc1[1]}:{loc2[0]},{loc2[1]}'
# print(query)
params = {
    'api-version': 1.0,
    'subscription-key': key,
    'query': query,
    'travelMode': travel_mode,
    'traffic': True,
    'ComputeTravelTimeFor': 'all'
}
response = requests.get(routeUrl, params=params).json()
print(response['routes'][0]['summary'])
