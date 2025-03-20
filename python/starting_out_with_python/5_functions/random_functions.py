import random

#The randrange() function works in a similar way to range().
number = random.randrange(10)       #Returns a number between [0, 10)
print(number)

number = random.randrange(5, 16)    #Returns a number between [5, 16)
print(number)

number = random.randrange(0, 21, 2)     #You can also specify step-sizes
print(number)
print()

#The random() function returns a floating point value between [0, 1.0)
number = random.random()
print(f"{number:.5f}")

#The uniform() works like random() but you can specify the range of values to select from.
#The bounds are inclusive.
number = random.uniform(1.0, 10.0)
print(f"{number:.5f}\n")

#If you want to generate the same sequence of pseudorandom numbers, you use the seed() function.
random.seed(10)
for i in range(10):
    print(random.randint(1, 10), end=', ')
print()