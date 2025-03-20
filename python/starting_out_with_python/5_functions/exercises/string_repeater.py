#Program to repeat a string a given number of times.

def string_repeater(string, number_of_repetitions):
    """Function to repeat a string a specified number of times."""
    data = string
    for i in range(number_of_repetitions - 1):
        data+= string
    return data

def main():
    """Mainline logic for the string repeater program."""
    string_to_repeat = input('Enter a string to repeat: ')
    number_of_repetitions = int(input('Enter the number of times you wish to repeat the string: '))

    string_to_repeat = string_repeater(string_to_repeat, number_of_repetitions)
    print(string_to_repeat)

if __name__ == '__main__':
    main()