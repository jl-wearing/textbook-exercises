#The prompt to the input function should tell the user
#what kind of information you're looking for.
name = input('Enter your name: ')
print(f"Hello, {name.title()}\n")

#Sometimes you'll want a prompt that's longer than one line.
#For example, you might want to tell the user why you're asking for certain input.
#You can assign the prompt to a variable first, then pass it as an argument to the input() function.
prompt = "If you share you're name, we can personalize the message you see."
prompt += "\nWhat is your first name? "
name = input(prompt)
print(f"Hello, {name.title()}\n")

#The input() function interprets the user input as a string.
#You can enclose the input function with int() to convert the input to an int.
#Works for float(), int().
age = int(input('Enter your age: '))
if age < 18:
    print("Too young to drive.")
else:
    print("Where's your whip?")