import requests

res = requests.get('https://www.weather.gov/')

print(res.text)