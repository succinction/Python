import requests

zip_code = input('enter a zip code: ')
units = "imperial" if input("Celseus : c | Fahrenheit : f ? ") == 'f' else "metric"
dct = {
	'metric': 'Celseus',
	'imperial': 'Fahrenheit'
}
payload = {'appid': 'b296ae1a65fde841767ad4a79ffa8d1d', 'zip': zip_code, 'units': units}

r = requests.get('http://api.openweathermap.org/data/2.5/weather', params=payload)

data = r.json()
print(r.url)
print()
print(data)
print()
print( "temperature: " , data['main']['temp'], dct[units])