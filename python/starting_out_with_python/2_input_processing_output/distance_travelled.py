#Program to calculate the distance travelled by a car.
#Distance = speed * time

#Input
speed = float(input('Enter your average speed in km/hr: '))
time = float(input('Enter the time elapsed in hours: '))

#Process
distance = speed * time

#Output
print(f"Distance Travelled: {distance:.2f}km.\n")