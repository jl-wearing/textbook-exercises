pizzas = ['Pepperoni', 'Triple Decker', 'Macon']
friend_pizzas = pizzas[:]

pizzas.append('Salami & Olive')
friend_pizzas.append('Vegetarian')

print()
print("My favourite pizzas are: ")
for pizza in pizzas:
    print(pizza.title(), end=' ')

print()
print("My friend's favourite pizzas are: ")
for pizza in friend_pizzas:
    print(pizza.title(), end=' ')
print()