age = int(input('Enter your age: '))

if age <= 4:
    print("Your admission costs $0.")
elif age < 18:
    print("Your admission costs $25.")
else:
    print("Your admission costs $40.")