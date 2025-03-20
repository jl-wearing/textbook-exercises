from name_function import get_formatted_name

while True:
    first = input('Enter your first name: ')
    if first == 'q':
        break

    last = input('Enter your last name: ')
    if last == 'q':
        break

    full_name = get_formatted_name(first, last)
    print(f"\nNeatly Formatted Name: {full_name}.\n")