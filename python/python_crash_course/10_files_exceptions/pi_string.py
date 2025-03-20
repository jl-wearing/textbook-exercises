from pathlib import Path

#get a pointer to the file.
path = Path('pi_digits.txt')

#read the contents from the file as a list.
contents = path.read_text().strip().splitlines()

#create a single string of the pi digits.
pi = ''
for value in contents:
    pi+= value

#convert to float.
pi = float(pi)

#output
print(pi)