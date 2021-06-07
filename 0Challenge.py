import requests
city = input("Enter City: ")
response = requests.get('https://api.openweathermap.org/data/2.5/weather/7f65701f025236c354d7754c5a4e0b71')
data = response.json()

weather = data['weather conversion']
print('weather conversion')


'''''
print(data)
print(data["weather"])

print"Weather is," )
'''''


