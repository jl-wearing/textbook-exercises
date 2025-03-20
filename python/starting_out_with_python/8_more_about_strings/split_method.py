#split() returns the words in a string as a list.
words = "one two three four"
list_of_words = words.split()
print(words)
print(list_of_words)

#By default, the split method uses spaces as separators.
#You can change how the split method operates by passing an argument.
data = '1/20/2025'
date_list = data.split('/')
print(date_list)