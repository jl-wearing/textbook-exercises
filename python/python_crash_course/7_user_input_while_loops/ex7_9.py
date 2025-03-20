sandwich_orders = ['dagwood', 'pastrami', 'egg sandwich', 'beef sandwich', 'pastrami', 'chicken sandwich', 'pastrami','tuna sandwich']
print("The deli has run out of pastrami.\n")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

#Confirm that all occurrences were removed.
for sandwich in sandwich_orders:
    print(f"\t{sandwich.title()}")