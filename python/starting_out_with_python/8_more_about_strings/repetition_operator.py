# This program demonstrates the repetition operator.

def main():
    """Using the repetition operator."""
    # Print 9 rows increasing in length.
    for count in range(1, 10):
        print('Z' * count)

    # Print 9 rows decreasing in length.
    for count in range(8, 0, -1):
        print('Z' * count)

# Call the main function.
if __name__ == '__main__':
    main()