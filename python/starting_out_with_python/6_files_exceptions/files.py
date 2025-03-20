#The open() function is used to open a file.
#r - is used to read from a file.
#w - is used to write to a file.
#a - is used to append to a file.
from io import UnsupportedOperation

try:
    footballers = open('files/footballers.txt', 'r')
except FileNotFoundError:
    pass

#Opening a file for writing.
#use r - to represent a raw string when specifying a path.
#This causes backslashes to be interpreted as literals and not escape characters.
sales_figures = open(r'/6_files_exceptions/files/data.txt', 'w')

#Processing the file.
#To write data to a file, use the write() method.
#The file must first be opened for writing, otherwise an error will occur.
try:
    sales_figures.write('P15 000 000.00')
    sales_figures.write('\nP25 000 000.00')
except UnsupportedOperation:
    print("File was never opened for writing.")

#Closing the file.
footballers.close()
sales_figures.close()