"""
Default dictionary
https://realpython.com/python-defaultdict/
"""

standard_dict = {
    'Piotr': 10,
    'John': 1,
}

print(standard_dict)

name = input('Provide a name: ')
points = int(input('Provide points: '))

if name not in standard_dict:
    standard_dict[name] = 0

standard_dict[name] += points

print(standard_dict)

print('-' * 60)


# the same thing but with defaultdict

from collections import defaultdict

users = defaultdict(int)
users['Piotr'] = 10
users['John'] = 1

print(users)

name = input('Provide a name: ')
points = int(input('Provide points: '))

users[name] += points

print(users)
print(users['Paul'])
