#Rather than breaking out of a loop entirely with the break clause,
#you can use the continue statement to jump to the beginning of the loop.

current_number = 0
while current_number <= 10:
    current_number+= 1
    if current_number % 2 == 0:
        print(current_number)
    else:
        continue