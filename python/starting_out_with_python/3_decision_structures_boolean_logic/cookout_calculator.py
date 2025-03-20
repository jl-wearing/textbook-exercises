#Program to calculate the number of ingredients required for a cookout.

#Constants
NUMBER_OF_HOTDOGS = 10      #number of hot dogs in a package.
NUMBER_OF_BUNS = 8          #number of buns in a package.

#Input
number_of_people = int(input('How many people are coming to the cookout: '))
per_person = int(input('How many hot dogs per person: '))

#Process
total_number_of_hotdogs = number_of_people * per_person

#Calculate number of hot dog packages.
if total_number_of_hotdogs % NUMBER_OF_HOTDOGS == 0:
    hot_dog_packages = total_number_of_hotdogs // NUMBER_OF_HOTDOGS
else:
    hot_dog_packages = (total_number_of_hotdogs // NUMBER_OF_HOTDOGS) + 1

#Calculate number of bun packages.
