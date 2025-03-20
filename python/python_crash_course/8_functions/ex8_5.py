#Write a function that takes a name of a city and its country.

def describe_city(city, country="Well I don't know"):
    print(f"{city.title()} is in {country.title()}.\n")

#Test the function with 3 different cities.
describe_city('sao paulo', 'brazil')
describe_city('gaborone', 'botswana')
describe_city('valencia')