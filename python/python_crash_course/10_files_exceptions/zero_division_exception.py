def divide(a, b):
    """Simple attempt to divide 2 numbers."""
    try:
        print(f"{a/b:.2f}")
    except ZeroDivisionError:
        print("You can't divide by zero.")

divide(10, 5)
divide(10, 2)
divide(10, 0)