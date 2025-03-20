#Program to calculate the average of 3 test scores.

#Input
scores = []
for i in range(3):
    score = float(input('Enter test score: '))
    scores.append(score)

#Process
total = 0
for score in scores:
    total = total + score
average = total / 3.0

#Output
if average >= 95:
    print(f"\nGood Job! Your average: {average:.2f}%.")
else:
    print(f"\nAverage: {average:.2f}%.")