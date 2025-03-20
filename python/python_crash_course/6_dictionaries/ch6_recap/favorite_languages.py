#Previous examples involved storing different kinds of information about one object.
#You can also use a dictionary to store one type of information about many objects.
#e.g to store the results of a poll:

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}
#It is good programming practice to add a comma after the last key-value pair,
#so you are ready to add a new key-value pair on the next line.
print(f"Sarah's favorite programming language is {favorite_languages['sarah'].title()}.\n")