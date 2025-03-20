from pathlib import Path

def count_words(path):
    """Count the approximate number of words in a file."""
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        pass
    else:
        #get a list of the words.
        words = contents.split()

        #get an approximate number of words in the file.
        num_words = len(words)

        #output
        print(f"The file {path} has about {num_words} words.")

#Testing the count_words() function.
files = ['alice.txt', 'moby_dick.txt', 'little_women.txt', 'big_java.txt', 'data_structures.txt', 'verity.txt']

for book in files:
    file = Path(book)
    count_words(file)