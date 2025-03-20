cities = {
    'paris': {
        'country': 'france',
        'population': 2_000_000,
        'fact': 'did you know the eiffel tower grows taller in summer.',
    },

    'cape town': {
        'country': 'south africa',
        'population': 5_000_000,
        'fact': 'did you know that cape town has a booming movie industry.',
    },

    'gaborone' : {
        'country': 'Botswana',
        'population': 250_000,
        'fact': 'did you know that gaborone is known for its diamond industy.',
    },
}

for key, value in cities.items():
    print(f"Information about {key.title()}: ")

    country = value['country'].title()
    population = value['population']
    fact = value['fact']

    #Output
    print(f"Country name: {country}")
    print(f"Population: {population}")
    print(f"Fun Fact: {fact}")
    print()