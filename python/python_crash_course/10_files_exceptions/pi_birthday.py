#program to determine if my birthday appears in the first 1 million digits of pi.
from pathlib import Path

#get a pointer to the file.
path = Path('pi_million_digits.txt')

#get the contents of the file as a list.
contents = path.read_text().strip().splitlines()

#get a single string representing pi.
pi = ''
for value in contents:
    pi+= value

#input
birthday = input('Enter your birthday, in the form mmddyy: ')
if birthday in pi:
    print("Your birthday appears in the first 1 million digits of pi!")
else:
    print("Your birthday does not appear in the first 1 million digits of pi.")