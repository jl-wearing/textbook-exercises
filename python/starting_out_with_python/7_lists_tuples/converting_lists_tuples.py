#The list function is used to convert a tuple to a list.
#The tuple function is used to convert a list to a tuple.

num_list = list(range(1, 6))
num_tuple = tuple(num_list)

#Output
print(num_list, num_tuple, sep='\n')

chars_tuple = ('a', 'b', 'c', 'd', 'e')
chars_list = list(chars_tuple)

#Output
print(chars_tuple, chars_list, sep='\n')