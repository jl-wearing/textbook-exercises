#Recapping what I learnt about reading and writing files.

def main():
    """Simple program to read from and write to a file."""
    #Open a file for reading.
    try:
        infile = open(r'files\recap.txt', 'r')
    except FileNotFoundError:
        pass

    #Read all the contents.
    contents = infile.read()

    #Close the file.
    infile.close()

    #Output all the data.
    print(contents)

    #Open a file for appending.
    infile = open(r'files\recap.txt', 'a')

    #Write data to the file.
    infile.write("\nMaximilian Pegasus\n")
    infile.write("Seto Kaiba\n")

    #Open the file for reading.
    infile = open(r'files\recap.txt', 'r')

    #Read all the contents.
    contents = infile.read()

    #Close the file.
    infile.close()

    #Output the contents.
    print(f"\n{contents}")

#Call the main function.
main()