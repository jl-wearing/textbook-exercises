from time import sleep

import lottery

#get a random numbers.
numbers = lottery.get_numbers(2)

#have user enter random numbers.
lucky_numbers = lottery.get_number_guess(2)

#number of rounds executed until player wins.
number_of_rounds = 1

print(lucky_numbers)
while lucky_numbers != numbers:
    print(numbers)
    sleep(2)

    number_of_rounds += 1

print(f"It took you {number_of_rounds} to win!")
print(numbers)
print(lucky_numbers)