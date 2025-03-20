from pathlib import Path

#get a pointer to the files to read.
cats = Path('cats.txt')
dogs = Path('dogs.txt')

try:
    #get the contents of the file.
    cat_contents = cats.read_text()
except FileNotFoundError:
    print(f"The file {cats} does not exist!")
else:
    try:
        #get the contents of the file.
        dog_contents = dogs.read_text()
    except FileNotFoundError:
        print(f"The file {dogs} does not exist!")
    else:
        #output
        print(f"\n{cat_contents}\n")
        print(f"{dog_contents}\n")