#Program to display the scores of 3 students.

#Constants used by the program.
SCORES = [[80, 74, 55],
          [100, 99, 100],
          [77, 88, 99]]

def main():
    """Simple program to display test scores."""
    i = 0
    for score_sheet in SCORES:
        print(f"Scores for student #{i + 1}: ")
        for score in score_sheet:
            print(score, end=' ')
        print('\n')
        i+= 1

#Call the main function.
if __name__ == '__main__':
    main()