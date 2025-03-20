list_1 = [1,2,3]
copy_1 = list_1 + []
copy_2 = list_1[:]

#Output
print(copy_1, copy_2, sep='\n')
boolean = list_1 is copy_1
print(boolean)
boolean = list_1 is copy_2
print(boolean)
print(copy_1 == copy_2 == list_1)