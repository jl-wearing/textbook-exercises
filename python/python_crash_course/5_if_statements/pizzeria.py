#all_toppings could be a tuple if the pizzeria has a stable selection of toppings.
all_toppings = ['extra cheese', 'macon', 'beef', 'pork', 'chicken', 'pineapple', 'mushrooms', 'pepperoni']

toppings = []
print('Enter your desired toppings: ')
result = 'y'
while result.lower() != 'q':
    topping = input('Enter topping: ')
    toppings.append(topping.lower().strip())
    result = input('Add another?: q to quit')

for topping in toppings:
    if topping in all_toppings:
        print(f"Adding {topping}.")
    else:
        print(f"Sorry, we don't have {topping}.")
print('Finished making your pizza!')