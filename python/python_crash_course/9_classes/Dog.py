class Dog:
    """A simple attempt to model a dog."""
    def __init__(self, name, age):
        """A dog is described by a name and age."""
        self.name = name
        self.age = age

    def sit(self):
        """Causes the dog to sit."""
        print(f"{self.name.title()} is now sitting.")

    def roll_over(self):
        """Causes the dog to roll over."""
        print(f"{self.name.title()} rolled over.")


#Testing the implementation of the class and its methods.
my_dog = Dog('kiwi', 7)

#Getters
print(f"My dog's name is {my_dog.name.title()}.")
print(f"My dog is {my_dog.age} years old.\n")

#Testing the sit() method.
my_dog.sit()

#Testing the roll_over() method.
my_dog.roll_over()