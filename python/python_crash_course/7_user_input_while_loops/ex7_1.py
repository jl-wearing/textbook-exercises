#Input
car = input('What manufacturer of rental car would you like?: ')

#Process
cars = ['subaru', 'kia', 'toyota', 'nissan', 'honda', 'hyundai']
if car.lower() in cars:
    print("\nI've got just the car for you!")
else:
    print("Sorry, we don't have that car in our inventory.")