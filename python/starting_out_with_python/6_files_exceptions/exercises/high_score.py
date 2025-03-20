#Program to determine the user with the highest score.

def main():
    """
    Simple program to read data from a file and determine
    the highest score.
    """
    try:
        #Get the filename from the user.
        file_name = input('Enter the filename: ')

        #Open the file for reading.
        infile = open(file_name, 'r')

        highest_score = -1
        highest_user = ''
        user = infile.readline().rstrip('\n')
        while user != '':
            #Get the score of the user.
            score = int(infile.readline())

            #Determine if the user's score is greater than the
            #current highest score.
            if score > highest_score:
                highest_user = user
                highest_score = score

            #Get the next record.
            user = infile.readline().rstrip('\n')

        #Close the file.
        infile.close()

        #Output the user with the highest score.
        print(f"\n{highest_user.title()} has the highest score with {highest_score} points!")
    except FileNotFoundError:
        print("The file does not exist!")
    except Exception as err:
        print(err)

#Call the main function.
if __name__ =='__main__':
    main()