# https://data.police.uk/docs/method/forces/

# urllib - build-in into python

import urllib.request
import json

with urllib.request.urlopen('https://data.police.uk/api/forces') as response:
    print(response)
    print(response.headers)
    print(response.status)
    response_data = response.read()
    print(response_data)

    # converting text (in JSON format) into python data structures
    response_data_json = json.loads(response_data)
    print(response_data_json)
    print(type(response_data_json))

    for force in response_data_json:
        print(force['id'], '-', force['name'])

