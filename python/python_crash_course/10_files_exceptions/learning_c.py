from pathlib import Path

#get a pointer to the file.
path = Path('learning_python.txt')

#get the contents of the file.
contents = path.read_text().strip()

#replace all occurrences of 'Python' with 'C'.
contents = contents.replace("Python", "C")

#output
print(contents)