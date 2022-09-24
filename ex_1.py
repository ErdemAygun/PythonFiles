"""
Create a console programme that will get the name of the file via sys.argv
then will open and read the file and display lines of the file
with proper numbering.

Example:
    python ex_1.py data2.txt

1: Hello world!
2: Hello world!
"""
import sys

try:
    file_name = sys.argv[1]

    with open(file_name) as file_handle:
        line_number = 1
        for line in file_handle:
            print(f'{line_number}: {line}', end='')
            line_number += 1

    with open(file_name) as file_handle:
        line_number = 1
        for line in file_handle:
            print(f'{line_number}: {line.rstrip()}')
            line_number += 1

    with open(file_name) as file_handle:
        for line_number, line in enumerate(file_handle, start=1):
            print(f'{line_number}: {line.rstrip()}')

except IndexError:
    print('You have to provide file name: python ex_1.py FILE_NAME')
    exit(1)  # anything different 0 is considered as an error or improper execution
except FileNotFoundError:
    print(f'File not found!')
    exit(1)
