correct_answer = 10
guess = int(input('Enter the number I am probably thinking of: '))

while guess != correct_answer:
    if guess > correct_answer:
        guess = int(input('Try guessing lower: '))
    elif guess < correct_answer:
        guess = int(input('Try guessing higher: '))

print(f"\nYou have guessed correctly. The correct answer was {correct_answer}.")