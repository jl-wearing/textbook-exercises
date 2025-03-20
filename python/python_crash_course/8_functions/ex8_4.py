#Modify the make_shirt() function such that each shirt is large by
#default.

def make_shirt(text='I love Python', size='large'):
    """Display information about a shirt."""
    print(f"Size of shirt: {size:10}")
    print(f"Message: {text:>19}")

#Make a large shirt and a medium shirt with the default message.
make_shirt()
make_shirt(size='medium')

#Shirt of any size with a different message.
make_shirt('I love Java', size='small')