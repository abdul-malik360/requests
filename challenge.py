
import requests

response = requests.get("https://openweathermap.org/api")
data = response.json()
print(data)
