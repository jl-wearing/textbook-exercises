#Program to adjust a recipe to make a cookie recipe.

#Recipe to make 48 cookies:
SUGAR = 1.5
BUTTER = 1
FLOUR = 2.75
COOKIES = 48

#Input
cookies = int(input('How many cookies would you like to make: '))

#Process
sugar = (SUGAR * cookies) / COOKIES
butter = (BUTTER * cookies) / COOKIES
flour = (FLOUR * cookies) / COOKIES

#Output
print(f"To make {cookies} cookies you need: ")
print(f"\t{sugar} cups of sugar,")
print(f"\t{butter} cups of flour and,")
print(f"\t{flour} cups of flour.\n")