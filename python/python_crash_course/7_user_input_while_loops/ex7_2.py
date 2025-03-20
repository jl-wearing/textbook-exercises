#Input
guest_number = int(input('How many people are in your dinner group?: '))

#Process
if guest_number >= 8:
    print("You will have to wait for a table to clear up!")
else:
    print("Right this way!")