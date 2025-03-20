"""Program to read csv files, specifically student scores."""

# Constants used by the program.
FILE_NAME = "test_scores.csv"
NUMBER_OF_SCORES = 5

def main():
    """Mainline logic for reading csv files."""
    # Open the file for reading.
    infile = open(FILE_NAME, 'r')

    # Read the content into a list.
    scores = infile.readlines()

    # Close the file.
    infile.close()

    #
    i = 0
    for raw_data in scores:
        true_scores = raw_data.split(',')

        # Determine the total score.
        total = 0.0
        for score in true_scores:
            total+= float(score)

        # Determine the average.
        average = total / NUMBER_OF_SCORES

        # Output
        print(f"Average for student #{i+1}: {average:.2f}")
        i+=1


# Call the main function.
if __name__ == '__main__':
    main()