import requests

response = requests.get('http://api.open-notify.org/astros.json')
json = response.json()

print('people currently in the space are:\n')
for person in json['people']:
    print(person['name'])



