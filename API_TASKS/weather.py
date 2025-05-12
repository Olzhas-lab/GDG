import requests

API_KEY="d9c2e3868821c67815d705dba3a9c924"
city_name=input("city name: ")
params={'q':city_name, 'appid': API_KEY, 'units':"metric"}
response=requests.get("https://api.openweathermap.org/data/2.5/weather", params=params)
data = response.json()
if "weather" in data:
    weather_info=data['weather'][0]['description']
    temperature=data['main']['temp']
    print(f"The weather parameter: {weather_info}")
    print(f"Temperature:{temperature}C")
    print(f"Feels like:{data['main']['feels_like']}C")
    print(f"The wind speed:{data['wind']['speed']}m/s")
else:
    print("Not found")
    
#print(response.status_code)