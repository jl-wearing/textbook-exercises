#Program to determine the score of a student.

#Input
grade = float(input('Enter your grade: '))

#Process
if grade >= 90:
    letter_grade = 'A'
elif grade >= 80 and grade < 90:
    letter_grade = 'B'
elif grade >= 70 and grade < 80:
    letter_grade = 'C'
elif grade >= 60 and grade < 70:
    letter_grade = 'D'
else:
    letter_grade = 'F'

#Output
print(f"\nYour Grade: {letter_grade}.")