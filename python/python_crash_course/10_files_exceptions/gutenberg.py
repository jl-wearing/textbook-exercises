from pathlib import Path

def count_word(path, word):
    """Count the number of occurrences of a word in a file."""
    try:
        #get the contents of the file.
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"The file {path} does not exist.")
    else:
        #get each line as a separate element to a list.
        lines = contents.splitlines()

        #count the number of occurrences of word in each line.
        count = 0
        for line in lines:
            if word in line:
                count+= 1

        #output
        print(f"The number of occurrences of {word} in {path} are: {count}.")

books = ['alice.txt', 'romeo_and_juliet.txt', 'big_java.txt']

for book in books:
    file = Path(book)
    count_word(file, "the ")