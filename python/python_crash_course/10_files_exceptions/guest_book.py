from pathlib import Path

#get a pointer to the file.
path = Path('guest_book.txt')

names = ""
prompt = "Enter your name: "
prompt+= "\nOr enter 'q' to quit: "

name = input(prompt)
while name != 'q':
    names+= name + "\n"

    name = input(prompt)

#write the names to the file.
path.write_text(names)