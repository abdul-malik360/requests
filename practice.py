import requests
city = ("cape town")
response = requests.get("https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=1185bd0b0eda694d9a5d672c24eecba1")
data = response.json()

print(data)


