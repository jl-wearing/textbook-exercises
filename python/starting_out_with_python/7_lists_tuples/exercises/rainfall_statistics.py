# Program to display rainfall statistics information.

# Constants used by the program.
MONTHS = ['january', 'february', 'march', 'april', 'may', 'june',
          'july', 'august', 'september', 'october', 'november', 'december']
NUMBER_OF_MONTHS = 12

def calculate_total_rainfall(rainfall_data):
    """Calculate the total rainfall in a year."""
    return sum(rainfall_data)

def calculate_average_rainfall(rainfall_data, total_rainfall):
    """Calculate the average rainfall received for each month."""
    return total_rainfall / len(rainfall_data)

def get_highest_monthly_rainfall(rainfall_data):
    """Determine the month that received the highest rainfall."""
    highest_rainfall = rainfall_data[0]
    highest_month = MONTHS[0]

    i = 1
    while i < len(rainfall_data):
        if rainfall_data[i] > highest_rainfall:
            highest_rainfall = rainfall_data[i]
            highest_month = MONTHS[i]
        i += 1

    return highest_month, highest_rainfall

def get_lowest_monthly_rainfall(rainfall_data):
    """Determine the month that received the lowest rainfall."""
    lowest_rainfall = rainfall_data[0]
    lowest_month = MONTHS[0]

    i = 1
    while i < len(rainfall_data):
        if rainfall_data[i] < lowest_rainfall:
            lowest_rainfall = rainfall_data[i]
            lowest_month = MONTHS[i]
        i += 1

    return lowest_month, lowest_rainfall

def get_rainfall_data():
    """Get the rainfall information from the user for each month."""
    rainfall_data = []
    for i in range(NUMBER_OF_MONTHS):
        rainfall = float(input('Enter the rainfall received in '
                               f'{MONTHS[i].title()}: '))
        rainfall_data.append(rainfall)

    return rainfall_data

def main():
    """Mainline logic for displaying rainfall statistics."""
    # Get the rainfall data from the user.
    rainfall_data = get_rainfall_data()

    # Calculate the total rainfall received in a year.
    total_rainfall = calculate_total_rainfall(rainfall_data)

    # Calculate the average rainfall received.
    average_rainfall = calculate_average_rainfall(rainfall_data, total_rainfall)

    # Determine the month with the highest and lowest rainfall.
    lowest_month, lowest_rain = get_lowest_monthly_rainfall(rainfall_data)
    highest_month, highest_rain = get_highest_monthly_rainfall(rainfall_data)

    # Output
    print(f"\nTotal Annual Rainfall:  {total_rainfall:.2f}mm.")
    print(f"Average Monthly Rainfall: {average_rainfall:.2f}mm.")
    print(f"Month with the highest recorded rainfall was {highest_month.title()} "
          f"with a recording of {highest_rain:.2f}mm of rain.")
    print(f"Month with the lowest recorded rainfall was {lowest_month.title()} "
          f"with a recording of {lowest_rain:.2f}mm of rain.")

# Call the main function.
if __name__ == '__main__':
    main()