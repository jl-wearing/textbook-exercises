#Create a function that makes a sandwich.

def make_sandwich(*foods):
    """Summarizes the sandwich we are about to make."""
    print("\nThese are the foods we are adding to the sandwich: ")
    for food in foods:
        print(f"- {food}")

make_sandwich('butter', 'egg', 'bacon')
make_sandwich('egg', 'cheese', 'polony')
make_sandwich('salami', 'lettuce', 'eggs', 'cheese')