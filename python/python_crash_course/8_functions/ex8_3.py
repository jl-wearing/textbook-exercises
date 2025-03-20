#Define a function that takes a shirt size and information to
#display on the shirt.

def make_shirt(size, text):
    """Display shirt with size and text."""
    print(f"Size of shirt ordered: {size}")
    print(f"Message to be printed: {text}\n")

#Test the function with positional arguments.
make_shirt('small', 'It is what it is')

#Test the function with keyword arguments.
make_shirt(text='Simply Lovely', size='large')
make_shirt(size='extra large', text='SSX')