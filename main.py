from sys import api_version
import requests 
import pprint
import temp_convert

API_KEY = 'cabdc41bb49b77826789d0949942a903'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

CITY_NAME = 'Thousand Oaks'

API_CALL = f'https://api.openweathermap.org/data/2.5/weather?q={CITY_NAME}&appid={API_KEY}'

response = requests.get(API_CALL).json()
pp = pprint.PrettyPrinter(indent = 2)
#pp.pprint(response)

temp_current = response['main']['feels_like']
temp_max = response['main']['temp_max']
temp_min = response['main']['temp_min']
temp = temp_current
temp_convert.CALC_FAH(temp)
print(temp)