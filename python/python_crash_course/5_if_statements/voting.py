age = int(input('Enter your age: '))

if age >= 18:
    print('You are old enough to vote!')
else:
    print(f'You have to wait {18 - age} year(s) before you can vote.')