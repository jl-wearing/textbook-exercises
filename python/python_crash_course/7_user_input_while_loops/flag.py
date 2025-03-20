#In simple situations, a while loop performs a task as long as a condition is True.
#For example, in a game, there can be many events that could cause a game to terminate.
#A flag allows a program to have multiple termination points.
#A program will run while the flag is True and terminate when any of several events set
#the flag to False.
#Therefore, a flag creates multiple termination points.

prompt = "\nTell me something and I will repeat it back to you."
prompt += "\nEnter 'quit' to terminate the program:"

flag = True
while flag:
    message = input(prompt)

    if message.lower() == 'quit':
        flag = False
    else:
        print(message) 