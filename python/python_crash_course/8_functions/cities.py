#Program to display information about a Country and the City it is in.

def describe_city(city, country='botswana'):
    """Display information about a city and the country it is located in."""
    print(f"{city.title()} is in {country.title()}.\n")

#Testing the describe_city() function.
#1. positional arguments.
describe_city('reykjavic', 'iceland')

#2. keyword arguments.
describe_city(country='south africa', city='cape town')

#3. default arguments
describe_city('gaborone')