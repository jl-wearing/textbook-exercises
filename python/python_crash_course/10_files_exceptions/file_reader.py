#Program to read from a file.
from pathlib import Path

#get the file to read
path = Path('pi_digits.txt')

#read the contents from the file
#read_file() returns the contents as a string.
content = path.read_text().strip()

#display the contents
print(content, '\n')

#splitlines() is used to work with individual lines of a file.
#it returns the content as a list of lines.
lines = content.splitlines()
print(lines)

#output
for line in lines:
    print(line)