# https://data.police.uk/docs/method/forces/

# https://pypi.org/project/requests/
# pip install requests

import requests

response = requests.get('https://data.police.uk/api/forces')

print(response)
print(response.content)

data = response.json()
print(type(data))
print(data)

for force in data:
    print(force['id'], '|', force['name'])
