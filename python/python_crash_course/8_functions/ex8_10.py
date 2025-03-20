#Define a function to move each message in one list to another.

messages = ['it is what it is', 'keep pushing', 'lets get it']
sent_messages = []

def send_messages(unsent_messages, sent_messages):
    """
    Display messages as they are sent.
    Sent messages are stored in a different list.
    """
    while unsent_messages:
        current_message = unsent_messages.pop()
        print(f"Sending message: {current_message}")
        sent_messages.append(current_message)

#Testing the function.
send_messages(messages, sent_messages)
print(messages)
print(sent_messages)