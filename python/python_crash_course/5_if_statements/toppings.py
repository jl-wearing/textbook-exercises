#Demonstrating the use of the inequality operator.
topping = input('Enter a topping: ')
if topping.lower() != 'anchovies':
    print('Hold the anchovies!')
print()

#Determining whether a particular value is in a list.
requested_toppings = ['pineapple', 'sauce', 'chicken']
if 'sauce' in requested_toppings:
    print('Great choice!')
else:
    print('Mushrooms would go great with that!')