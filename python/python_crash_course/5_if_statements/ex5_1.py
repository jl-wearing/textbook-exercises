car = 'subaru'
print("is car == 'subaru'? I predict True.")
print(car == 'subaru')
print()

toppings = []
print('Enter at least 3 toppings: ')
for value in range (1, 4):
    topping = input(f'Enter topping {value}: ')
    toppings.append(topping)

if 'chicken' in toppings:
    print('Would you like some chicken sauce with that?: y/n')
    response = input()
    if response.lower() == 'y':
        toppings.append('chicken sauce')
        print('Added chicken sauce to your list of toppings!')
    else:
        print('Okie dokie!')

if 'mushrooms' not in toppings:
    response = input('Would you like to add some mushrooms with that?: y/n')
    if response.lower() == 'y':
        toppings.append('mushrooms')
else:
    print('Not adding mushrooms!')