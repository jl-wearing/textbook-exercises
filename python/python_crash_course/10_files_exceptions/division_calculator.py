def divide(a, b):
    """A simple attempt to divide 2 numbers."""
    try:
        print(f"{a/b:.2f}")
    except ZeroDivisionError:
        print("You can't divide by zero!")
    except TypeError:
        print("enter numbers, you idiot!")


divide('a', 2)
divide(2, 4)
divide(2, 0)