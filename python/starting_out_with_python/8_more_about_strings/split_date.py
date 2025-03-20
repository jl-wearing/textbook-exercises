# Program to split a date.
# Constant used by the program.
DATE = '11/9/2001'

def main():
    """Mainline logic for splitting dates."""
    dates = DATE.split('/')
    # Output
    print(f"Day: {dates[0]}")
    print(f"Month: {dates[1]}")
    print(f"Year: {dates[2]}")

# Call the main function.
if __name__ == '__main__':
    main()