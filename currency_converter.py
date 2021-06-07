import requests


response = requests.get("https://v6.exchangerate-api.com/v6/5ad18b7d2e7ba4449612b2a8/latest/USD")
data = response.json()
print(data)
