height = int(input("How tall are you, in centimeters: "))
HEIGHT_LIMIT = 155

if height >= HEIGHT_LIMIT:
    print("\nYou're tall enough to ride!")
else:
    print("\nUnfortunately, you cannot ride the rollercoaster. Sorry!")