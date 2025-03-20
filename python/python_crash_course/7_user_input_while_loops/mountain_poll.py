#We can use while loop to gather data in a dictionary.
responses = {}

polling_active = True
while polling_active:
    #Prompt for the person's name and response.
    name = input('\nEnter your name: ')
    response = input('Which city would you like to visit some day?: ')

    #Store the response in a dictionary.
    responses[name] = response

    #Find out if anyone else will take the poll.
    repeat = input("\nWould you like to let another person respond?, (yes/no): \n")
    if repeat == 'no':
        polling_active = False

#Display the results.
print("\n-------Poll Results-------\n")
for name, response in responses.items():
    print(f"{name.title()} would like to visit {response.title()} someday.")