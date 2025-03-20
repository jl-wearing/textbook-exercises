#Python function to reverse a string.

def reverse_string(string):
    """Reverses a string."""
    reverse = ""
    index = len(string) - 1

    while(index >= 0):
        reverse+= string[index]
        index -= 1
    
    return reverse

def palindrome(string):
    "Checks if a word is a palindrome."
    reverse = reverse_string(string)

    return string == reverse

#Testing the reverse_string() function.
word = input('Enter a word to reverse: ')
print(f"The reverse of {word} is {reverse_string(word)}.\n")

#Testing the palindrome function.
word = input('Enter a word to determine if it is a palindrome: ')
if palindrome(word):
    print(f"{word} is a palindrome.\n")
else:
    print(f"{word} is not a palindrome.\n")