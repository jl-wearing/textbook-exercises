while True:
    print("\nEnter 2 numbers and I will try to divide them.")
    first_number = input('\nEnter first number: ')
    second_number = input('Enter second number: ')

    if first_number == 'q' or second_number == 'q':
        break

    try:
        answer = int(first_number) / int(second_number)
    except ValueError:
        print('enter numbers, not strings, you idiot.')
    except ZeroDivisionError:
        print("You can't divide by zero!")
    else:
        print(f"{answer:.2f}")