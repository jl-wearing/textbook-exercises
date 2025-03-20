#endswith(substring) returns true if a string ends with substring.
string = 'tomatoes'
empty = ''
print(string.endswith('toes'))
print(string.endswith('ss'))
print(empty.endswith(''))

#find(substring) returns the lowest index where substring is found.
#returns -1 if substring is not found.
string = "cows dogs caramel"
print(string.find('car'))
print(string.find('poo'))
print(empty.find(''))

#replace(old, new) replaces all occurrences of old with new.
string = "cats dogs dogs cats cars bars"
print(string.replace("cats", "poo"))
print(string.replace("owls", "domestos"))

#startswith() returns true if a string starts with substring.
print(string.startswith("cats"))