from random import randint

def get_numbers(size):
    """Get a list of numbers."""
    if size <= 0:
        print("Size cannot be zero or less.")
    else:
        numbers = []
        for i in range(size):
            numbers.append(randint(1, size))

        #convert the numbers to strings.
        dat = []
        while numbers:
            #retrieve a number.
            element = numbers.pop()

            #add the string number to dat.
            dat.append(str(element))

        #reverse the list to maintain the original order.
        dat.reverse()

        return dat

def get_letters(size):
    if size < 0:
        print("No negative letter exists.")
    else:
        letters = []
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        for i in range(size):
            letters.append(alphabet[randint(0, 25)])

        return letters

def get_letter_guess(size):
    """Retrieve a guess from the user."""
    guess = input(f"Enter a {size}-letter guess: ")
    return list(guess)

def get_number_guess(size):
    """Retrieve a guess from the user."""
    guess = input(f"Enter a {size}-number guess: ")
    return list(guess)
