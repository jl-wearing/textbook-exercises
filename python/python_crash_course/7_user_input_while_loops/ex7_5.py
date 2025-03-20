prompt = "\nEnter your age to determine your movie ticket price or '-1' to exit: "

active = 0
while active != -1:
    message = input(prompt)
    age = int(message)

    if age < 3:
        price = 0.00
    elif age >=3 and age <= 12:
        price = 10.00
    else:
        price = 15.00
    
    #Output
    print(f"\nYour fare is ${price:.2f}")