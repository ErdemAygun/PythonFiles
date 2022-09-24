"""
Data formats:
- CSV
- plain text
- XLSX
- XML - https://en.wikipedia.org/wiki/XML
- YAML - https://en.wikipedia.org/wiki/YAML
- JSON - https://en.wikipedia.org/wiki/JSON
"""

import json

data = json.load(open('data_formats/data.json'))

print(data)
print(type(data))
print(data['year'])
print(data['students'][0]['first_name'])

data['students'].append({
    'first_name': 'John',
    'last_name': 'Doe'
})

json.dump(data, open('data_formats/data2.json', 'w'), indent=4)
