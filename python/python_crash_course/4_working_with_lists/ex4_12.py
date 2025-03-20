foods = ['lemon', 'icing', 'sugar', 'flour']
copy = foods[:]

copy.append('milk')
copy.append('eggs')

print("Ingredients for a cake: ")
for ingredient in foods:
    print(ingredient, end=' ')
print()

print("Similar cake ingredients: ")
for ingredient in copy:
    print(ingredient, end=' ')
print()