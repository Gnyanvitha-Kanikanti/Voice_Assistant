import requests
api_address = "http://api.openweathermap.org/data/2.5/weather?q=Hyderabad&appid=07c674619d2387b24e701ef18a1e6722"
json_data = requests.get(api_address).json()
def temp():
    temprature = round(json_data['main']['temp']-273, 1)
    return temprature
def des():
    description = json_data['weather'][0]['description']
    return description