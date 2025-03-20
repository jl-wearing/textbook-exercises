def print_models(unprinted_designs, printed_designs):
    """
    Simulate printing each design until none are left.
    Move each design to completed designs after printing.
    :param unprinted_designs: A list of models not printed.
    :param printed_designs: A list of printed models.
    """
    while unprinted_designs:
        #retrieve a design to work on.
        current_design = unprinted_designs.pop()

        #work on current design.
        print(f"Currently Printing: {current_design.title()}")

        #add printed model to completed designs.
        printed_designs.append(current_design)

def show_completed_models(completed_designs):
    """
    Display all models that were completed.
    :param completed_designs: The list of designs that were printed.
    """
    print(f"\nThe following models have been completed: ")
    for design in completed_designs:
        print(f"\t{design.title()}")