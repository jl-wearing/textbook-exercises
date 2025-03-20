#The programs you use everyday most likely contain while loops.
#For example, a menu or game needs a while loop to keep running as long as you want it working.

prompt = "\nTell me something and I will repeat it back to you."
prompt += "\nEnter 'quit' to terminate the program:"

message = ""
while message != "quit":
    message = input(prompt)
    
    if message != 'quit':
        print(message)