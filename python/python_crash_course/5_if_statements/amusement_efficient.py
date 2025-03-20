age = int(input('Enter your age: '))
if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40
print(f"Your admission costs ${price}.")