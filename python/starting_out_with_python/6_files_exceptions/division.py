#Simple program to divide 2 numbers.

def main():
    """Divide the first number by the second number."""
    try:
        print("This program divides 2 numbers.")
        #Get input from the user.
        first_number = float(input('Enter the first number: '))
        second_number = float(input('Enter the second number: '))

        result = first_number / second_number
        return result
    except ValueError:
        print("Enter correct numerical figures.")
    except TypeError:
        print("Enter correct numerical figures.")
    except ZeroDivisionError:
        print("Can't divide by zero!")
    except Exception as err:
        print(err)

#Call the main function.
if __name__ == '__main__':
    main()