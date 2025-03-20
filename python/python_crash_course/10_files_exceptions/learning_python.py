from pathlib import Path

#get a pointer to the file.
path = Path('learning_python.txt')

#get the contents of the file.
all_content = path.read_text().strip()
#get the contents as a list.
contents = all_content.splitlines()

#output the entire content
print(all_content, '\n')

#output each line
for data in contents:
    print(data)
print()