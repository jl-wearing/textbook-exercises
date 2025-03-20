from pathlib import Path

#get a pointer to the file.
path = Path('alice.txt')

#get the contents of the file.
try:
    contents = path.read_text(encoding='utf-8')
except FileNotFoundError:
    print(f"Sorry, the file {path} does not exist.")
else:
    #obtains a list of each word.
    words = contents.split()

    #get an approximate number of words.
    num_words = len(words)

    #output
    print(f"The file {path} has about {num_words} words.")