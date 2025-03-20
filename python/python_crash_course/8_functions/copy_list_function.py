#Sometimes you may want to prevent a function from modifying a list.
#The solution is to pass a copy into the function.

def print_models(unprinted_models, completed_models):
    """
    Simulate printing each design until none are left.
    Move each design to completed designs after printing.
    """
    while unprinted_models:
        current_design = unprinted_models.pop()
        print(f"Printing Model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe following designs have been printed:")
    for design in completed_models:
        print(f"{completed_models}")

#Testing the functions with a copy.
unprinted_models = ['robot pendant', 'dodecahedron', 'pentagon', 'flying saucer']
completed_models = []

#Passing a copy to prevent the function from modifying the original list.
print_models(unprinted_models[:], completed_models)
show_completed_models(completed_models)

#Display the elements in the lists.
print('\n', unprinted_models, sep='')
completed_models.reverse()
print(completed_models)