messages = ['keep pushing', 'it is what it is', 'make it count']
sent = []

def show_messages(data):
    """Display the data in the list."""
    for message in data:
        print(message)
    print()

def send_messages(data, sent_items):
    """Send messages and move them to sent items."""
    while data:
        #retrieve a message.
        current_message = data.pop()

        #send message
        print(f"sending: {current_message}")
        #add to sent_messages.
        sent_items.append(current_message)
    print()

#Testing the show_message() method.
show_messages(messages)

#Testing the send_messages() method.
send_messages(messages, sent)
print(messages)
print(sent)
