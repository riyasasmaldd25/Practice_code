# API KEY = e4c0a57862a14ac5b94195644250609

import requests

city = input('Enter the city you want to get the weather report on\n')
url ='http://api.weatherapi.com/v1/current.json?key=e4c0a57862a14ac5b94195644250609&q='+city+'&aqi=no'
response = requests.get(url)
json = response.json()

print('The temperature in '+ city+ ' is')

temp = json.get('current').get('temp_c')

print(temp)

description = json.get('current').get('condition').get('text')
print('todays weather in '+ city+ ' is:', description)