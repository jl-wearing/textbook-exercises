from pathlib import Path

#input
name = input('Enter your name: ')

#get a pointer to the file.
path = Path('guest.txt')

#write the name to the file.
path.write_text(name)