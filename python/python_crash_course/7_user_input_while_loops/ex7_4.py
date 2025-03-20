toppings = []

prompt = "Enter your desired toppings."
prompt += "\nInput 'quit' to stop:\n"
active = True
while active:
    topping = input(prompt)

    if topping == 'quit':
        active = False
    else:
        print(f"\nAdding {topping.lower()} to your pizza.\n")
        toppings.append(topping)

print(f"Here are the toppings you requested: ")
if toppings:
    for topping in toppings:
        print(f"\t{topping.lower()}")
else:
    print(f"You entered no toppings.")