# Program to calculate how many calories are in each macronutrient.

# Constants used by the program.
CALORIES_IN_FAT = 9     # calories in 1 gram of fat
CALORIES_IN_PROTEIN = 4 # calories in 1 gram of protein
CALORIES_IN_CARB = 4    # calories in 1 gram of carbohydrates

def get_input():
    """Get macronutrient input from the user."""
    user_input = input('Enter your choice: ')
    return user_input

def display_menu():
    """Get input from the user."""
    print("This program converts your macronutrients to calories.")
    print("These are your options: ")
    print("1)Convert grams of fat")
    print("2)Convert grams of carbohydrates")
    print("3)Convert grams of protein")
    print("q)Quit the program")
    print("\nPlease enter your choice: ")

def calculate_calories_of_fat(grams_of_fat):
    """Convert grams of fat to calories."""
    return grams_of_fat * CALORIES_IN_FAT

def calculate_calories_of_carb(grams_of_carbs):
    """Convert grams of carbohydrates to calories."""
    return grams_of_carbs * CALORIES_IN_CARB

def calculate_calories_of_protein(grams_of_protein):
    """Convert grams of protein to calories."""
    return grams_of_protein * CALORIES_IN_PROTEIN

def how_many_grams_to_convert():
    """Get input on how many grams to convert."""
    user_input = input('How many grams would you like to convert: ')
    return user_input

def main():
    """Mainline logic for converting macronutrients to calories"""
    # Display the menu of options.
    display_menu()

    # Get input from the user.
    user_input = get_input().lower()
    while (user_input != '1' or user_input != '2' or user_input != '3'
                or user_input != 'q'):
        print("Please enter either 1, 2, 3 or q as options please: ")
        user_input = get_input()



# Call the main function.
if __name__ == '__main__':
    main()