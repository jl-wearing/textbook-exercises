numbers = list(range(1, 10))
for value in numbers:
    if value == 1:
        print(f'{value}st', end=' ')
    elif value == 2:
        print(f'{value}nd', end=' ')
    elif value == 3:
        print(f'{value}rd', end=' ')
    else:
        print(f'{value}th', end=' ')
print()