#Whitespace refers to any non-printing characters like tabs, spaces, or end-of-lines.

print("Languages: \n\tPython\n\tC\n\tJava")

#Python has 3 methods to remove whitespace from text: lstrip(), rstrip(), strip()
#These methods are mainly used to clean up user input before it is stored.
#Stripping is essential especially when testing the equality of 2 strings, e.g. when a user logs in with their username.

lang = " Python "
print(lang.lstrip())
print(lang.rstrip())
print(lang.strip())