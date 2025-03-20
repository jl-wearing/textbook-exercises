list_1 = [1,2,3] * 2
list_2 = [0] * 2
list_3 = list_1 + list_2

#Output
print(list_1, list_2, list_3, sep='\n')
list_3.append(15)
print(list_3[-1])