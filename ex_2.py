"""
Write a programme that will read the log file with users activity in the system.
Display the information on how much time user spent in the system as the sum of
numbers read from the file.

$ python ex_2.py logs_simple.txt
Time in the system:
- user-1: 92 s
- user-2: 51 s
- user-3: 20 s
"""

import sys
from collections import defaultdict

try:
    file_name = sys.argv[1]

    with open(file_name) as file_handle:
        total_time = defaultdict(int)
        for line in file_handle:
            user, time = line.split(';')  # user-4;57
            if user not in total_time:  # without default dict
                total_time[user] = 0  # without default dict
            total_time[user] += int(time)

    print(total_time)

    for user, user_total_time in total_time.items():
        print(f'{user}: {user_total_time}')

except IndexError:
    print('You have to provide file name: python ex_2.py FILE_NAME')
    exit(1)  # anything different 0 is considered as an error or improper execution
except FileNotFoundError:
    print(f'File not found!')
    exit(1)