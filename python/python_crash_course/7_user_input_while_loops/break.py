#The break clause is used to terminate a loop immediately
#and jump to the statements after the loop body.

prompt = "\nEnter the name of a city you have visited."
prompt += "\nEnter 'quit' to terminate the program:\n"

cities = []
flag = True
while flag:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        cities.append(city.lower())
        print(f"\nI'd love to go to {city.title()}.")

if cities:
    print(f"Here are the cities you mentioned: {cities}.\n")
else:
    print(f"You mentioned no cities.")

#A loop with a while True statement will run forever unless it reaches a break statement.