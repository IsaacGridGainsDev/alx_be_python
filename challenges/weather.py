import requests

weather_data = requests.get("https://api.weatherapi.com/v1/current.json?key=YOUR_API_KEY&q=London")

try:
	weather_info = weather_data.json()
except ValueError:
	print("There is an issue")
else:
	print(f"Temperature: {weather_info['current']['temp_c']} C")
	print(f"Condition: {weather_info['current']['condition']['text']}")
