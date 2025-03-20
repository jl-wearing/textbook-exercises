#Program to calculate the number of grapevines that can be planted in a row.
#v = (r - 2e) / s, where:
#v = number of grapevines that will fit in a row.
#r = length of the row.
#e = amount of space used by an assembly.
#s = space between vines.

#Input
r = float(input('Enter the length of the row in feet: '))
e = float(input('Enter the amount of space used by an end-post assembly: '))
s = float(input('Enter the amount of space between vines: '))

#Process
v = (r - 2* e) / s

#Output
print(f"\nNumber of grapevines that can be planted in each row: {v:.0f}.")