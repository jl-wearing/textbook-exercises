#Program to make a t-shirt with a size and text to be displayed.

def make_shirt(size_of_shirt='large', text_to_be_displayed='I love Python!'):
    """Display information about a t-shirt."""
    print(f"Information about your t-shirt: ")
    print(f"\tSize: {size_of_shirt.title():>13}")
    print(f"\tFront Label: {text_to_be_displayed}\n")

#Testing the make_shirt() function.
#1. Positional Arguments.
make_shirt('medium', 'It is what it is')

#2. Keyword Arguments.
make_shirt(text_to_be_displayed='Keep Pushing', size_of_shirt='large')

#3. Default Arguments
make_shirt()
make_shirt('medium')