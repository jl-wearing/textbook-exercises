#Program to calculate the percentage of males and females in a class.

#Input
number_of_students = int(input('Enter the number of students in the class: '))
girls = int(input('Enter the number of girls: '))
boys = number_of_students - girls

#Process
percentage_boys = (boys / number_of_students) * 100
percentage_girls = (girls / number_of_students) * 100

#Output
print(f"\nPercentage of boys: {percentage_boys:.2f}%.")
print(f"Percentage of girls: {percentage_girls:.2f}%.\n")