"""
Files

read - whole file
readlines - list of strings, lines from the file

https://stackoverflow.com/questions/16208206/confused-by-python-file-mode-w/16212401#16212401
"""

file_handle = open('data.txt')
file_content = file_handle.read()
print(file_content)
file_handle.close()  # closing file handle


file_handle = open('data.txt')
file_content = file_handle.readlines()
print(file_content)
file_handle.close()  # closing file handle


file_handle = open('data2.txt', 'w+')
file_handle.write('Hello world!\n')
file_handle.write('Hello world!')
file_handle.close()


file_handle = open('data2.txt', 'w+', encoding='utf-8')
file_handle.write('Hello world!\n')
file_handle.write('Hello world!')
file_handle.close()


# with compound statements we don't have to close the file,
# the file will be closed automatically

with open('data.txt', 'r') as file_handle:
    print(file_handle.readlines())

# after exiting "with" statement, file will be closed

print('-' * 60)

with open('data.txt', 'r') as file_handle:
    for line in file_handle:
        print(line)

print('-' * 60)

# r"" - r-string / raw string, python is not trying to escape any characters within this string
r"""
https://docs.python.org/3/library/os.html#os.DirEntry
. - represents current directory
.. - goes one level up
More on os module: https://realpython.com/working-with-files-in-python/
Relative paths - relative to the current file
Absolute paths 
    on Windows:
        C:\Documents\Newsletters\Summer2018.pdf
    on Mac/Linux:
        /Users/gradzinski/Documents/Newsletters/Summer2018.pdf
"""

import os

# dir_content = os.scandir('.')
# dir_content = os.scandir('..')
dir_content = os.scandir('my_data')  # relative path
dir_content = os.scandir('../1_basics_pgg')  # relative path
# dir_content = os.scandir('/Users/gradzinski/dev_home/alx_python-analiza/szkolenia/2022_07_ZDL_W/dap_20220711/5_files_pgg')  # absolute path
print(dir_content)
for element in dir_content:
    print(element)
    print(element.name)
    print(element.path)
    print(element.is_dir())
    print(element.is_file())
    print()

# cron - tool for executing programs every given time, like every hour

# often we have to provide some additional information to our script

print('-' * 60)

"""
To execute this code, open terminal and then
cd 5_files_pgg
python files_intro.py data.txt
"""

import sys

print(sys.argv)

with open(sys.argv[1]) as file_handle:
    for line in file_handle:
        print(line)

"""
If you want to create more complicated scripts, 
that can get more parameters it's worth checking
argparse module
https://docs.python.org/3/library/argparse.html
https://realpython.com/command-line-interfaces-python-argparse
"""

print('-' * 60)

# enumerate
names = ['Piotr', 'John', 'Mark']

for number, name in enumerate(names, start=10):
    print(number, name)


print('-' * 60)

line = 'user-4;57'
user, time = line.split(';')
user, time = ['user-4', '57']

print(line.split(';'))
print(user)
print(time)
