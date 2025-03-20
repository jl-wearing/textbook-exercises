#Program to write to a file.
from pathlib import Path

#get a pointer to a file.
path = Path('programming.txt')

#write_text() is used to write data to a file.
path.write_text('I love Python programming.')