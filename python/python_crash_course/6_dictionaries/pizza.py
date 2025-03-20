#It is sometimes useful to put a list in a dictionary.
#For example, a list of toppings can be one aspect of the pizza you're describing.

pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'salami', 'pineapple']
}

#Summarize the order.
print(f"You've ordered a {pizza['crust']}-crust pizza with the following toppings:")
for topping in pizza['toppings']:
    print(f"{topping}")
print()