#Program to determine if a student passed based on a points system.

#Constants
DISTINCTION_GRADE = 80
CREDIT_GRADE = 60

#Input
test1 = int(input('Enter first score: '))
test2 = int(input('Enter second score: '))
exam = int(input('Enter exam score: '))

#Process
total = test1 + test2 + exam
if exam < 25 or total < 50:
    print("\nFail.")
elif total > DISTINCTION_GRADE:
    print("Distinction.")
elif total < DISTINCTION_GRADE and total > CREDIT_GRADE:
    print("\nCredit.")
elif total < CREDIT_GRADE:
    print("\nPass.")