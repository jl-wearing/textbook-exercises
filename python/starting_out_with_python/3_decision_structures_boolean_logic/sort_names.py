#Program to sort 2 names in lexigrographical order.

#Input
name1 = input('Enter first name: ')
name2 = input('Enter second name: ')

#Process
if name1 < name2:
    print(f"\n{name1}\n{name2}")
else:
    print(f"{name2}\n{name1}")