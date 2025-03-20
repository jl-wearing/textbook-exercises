#Define a function that takes a list and prints each message.

messages = ['it is what it is', 'keep pushing', 'lets get it']

def show_messages(messages):
    """Print the statements in the list."""
    if messages:
        for message in messages:
            print(message)
    else:
        print("There are no messages.")

#Testing the function.
show_messages(messages)