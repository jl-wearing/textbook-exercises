responses = {}
poll_active = True

while poll_active:
    name = input('Enter your name: ')
    response = input('If you could have one thing in the world, what would it be?: ')

    #Add the data to the dictionary.
    responses[name] = response

    #Check if another person wants to take the poll.
    repeat = input('Would another person like to take the poll?, (yes/no)?: ')
    if repeat == 'no':
        poll_active = False
print()

#Display the results.
for name, response in responses.items():
    print(f"The one thing {name.title()} wants is {response}.")
