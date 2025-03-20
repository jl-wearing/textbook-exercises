#program to read from a file.
from pathlib import Path

#get a pointer to the file.
path = Path('pi_million_digits.txt')

#get the contents of the file as a list.
contents = path.read_text().strip().splitlines()

#convert to a single string.
pi = ''
for value in contents:
    pi+= value

#display to the first 50 decimal places.
print(pi[:52])