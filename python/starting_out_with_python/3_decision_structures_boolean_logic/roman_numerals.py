#Program to display roman numeral equivalent of numbers 1 through 10.

#Input
roman_numerals = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"]
num = int(input('Enter a number to convert: '))

if num > 0 and num <= len(roman_numerals):
    print(f"\n{num} == {roman_numerals[num - 1]}")
else:
    print("Invalid number entered.")