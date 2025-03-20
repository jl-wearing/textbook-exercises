#Program to assign random numbers to a 2D list.
import random

def main():
    """Mainline logic for assigning numbers to a 2D list."""
    while True:
        try:
            # Get the number of rows for the 2D list.
            number_of_rows = get_row_size()

            # Get the number of columns for the 2D list.
            number_of_columns = get_column_size()
            break
        except ValueError:
            print("Please enter valid numbers!")
        except TypeError:
            print("Please enter valid numbers!")
        except Exception as err:
            print(f"An error has occurred: {err}")

    #Generate random numbers and store them in the 2D list.
    twod_list = []
    for row in range(number_of_rows):
        row_data = []
        for column in range(number_of_columns):
            row_data.append(random.randint(1, 100))
        twod_list.append(row_data)

    #Print the elements in the resulting 2D list.
    print_list(twod_list)

def get_row_size():
    """Determine the number of rows for the 2D list."""
    number_of_rows = int(input('Enter the number of rows: '))
    return number_of_rows

def get_column_size():
    """Determine the number of columns for the 2D list."""
    number_of_columns = int(input('Enter the number of columns: '))
    return number_of_columns

def print_list(data):
    """Display the elements in a 2D list."""
    for row in data:
        for column in row:
            print(column, end=' ')
        print()

#Call the main function.
if __name__ == '__main__':
    main()