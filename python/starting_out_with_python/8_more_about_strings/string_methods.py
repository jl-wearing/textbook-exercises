#The isalnum() method returns True if a string contains only alphabetic
#or numeric characters and is at least one character in length.
string = '123asb'
string2 = 'abc'
string3 = '123'
string4 = ',.,.'
print(string.isalnum(), string2.isalnum(), string3.isalnum(), string4.isalnum(), sep=' ')


#The isalpha() method returns True if a string contains only alphabetic
#characters and is at least one character in length.
print(string.isalpha(), string2.isalpha(), string3.isalpha(), string4.isalpha(), sep=' ')

#The isdigit() method returns True if a string contains only digits
# #and is at least one character in length.
print(string.isdigit(), string2.isdigit(), string3.isdigit(), string4.isdigit())

#islower() returns True if all the alphabetic letters in the string are lowercase.
print(string.islower(), string2.islower(), string3.islower(), string4.islower(), sep=' ')

#isupper() returns True if all the alphabetic letters in the string are uppercase.
string5 = 'ABC'
print(string.isupper(), string2.isupper(), string3.isupper(), string4.isupper(), string5.isupper(), sep=' ')

#isspace() returns true if a string contains only whitespace.
string6 = ''
string7 = '\n\t'
string8 = '     '
print(string.isspace(), string2.isspace(), string3.isspace(), string4.isspace(), string5.isspace(), sep=' ')
print(string6.isspace(), string7.isspace(), string8.isspace())