"""
Fetch data from this endpoint:
http://api.nbp.pl/api/exchangerates/tables/A/?format=json

and display a list of currency codes and rates.
"""

import requests

response = requests.get('http://api.nbp.pl/api/exchangerates/tables/A/?format=json')
data = response.json()

for rate in data[0]['rates']:
    print(rate['code'], '=', rate['mid'])
