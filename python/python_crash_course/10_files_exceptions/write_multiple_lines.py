#To write multiple lines to a file, you must first build a string containing all the contents to be written.
from pathlib import Path

#get a pointer to the file.
path = Path('programming2.txt')

#construct the content to be written.
content = "I love Python programming."
content+= "\nI find Java to be quite complex."
content+= "\nI also love working with data."

#write contents to file.
path.write_text(content)

#write_text() overwrites data if the file exists.