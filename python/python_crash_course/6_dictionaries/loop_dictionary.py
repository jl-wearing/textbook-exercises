alien_0 = {'color': 'green', 'points': 5, 'speed': 'slow'}


for value in alien_0:
    print(f"Key: {value}, value: {alien_0[value]}")
print("\n")

#There are 3 ways to loop through a dictionary:
#1. To loop through all key-value pairs.
#2. To loop through the keys.
#3. To loop through the values.

#Looping through all key value pairs.
#The keys() method returns a list of all the keys.
for key, value in alien_0.items():
    print(f"Key: {key}")
    print(f"Value: {value}\n")
print()