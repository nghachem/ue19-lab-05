import requests
response = requests.get("https://official-joke-api.appspot.com/random_joke")
if response.status_code == 200:
  print(response.json())
else:
  print('Erreur', response.status_code)
