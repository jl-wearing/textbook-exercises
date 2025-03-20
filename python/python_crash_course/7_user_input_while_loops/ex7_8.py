sandwich_orders = ['dagwood', 'egg sandwich', 'beef sandwich', 'chicken sandwich', 'tuna sandwich']
finished_orders = []

while sandwich_orders:      #As long as sandwich_orders is not empty.
    current_order = sandwich_orders.pop()

    #Output
    print(f"I made your {current_order}.")
    finished_orders.append(current_order)

print("\nMy shift is over. These are the sandwiches I made: ")
for sandwich in finished_orders:
    print(f"\t{sandwich.title()}")
