from city_functions import get_formatted_city_country

def test_city_country():
    """Do instances like Santiago & Chile work?"""
    formatted_name = get_formatted_city_country('santiago', 'chile')
    assert formatted_name == "Santiago, Chile"

def test_city_country_population():
    """Do instances like Santiago, Chile, 5_000_000 work?"""
    formatted_name = get_formatted_city_country('santiago', 'chile', 5_000_000)
    assert formatted_name == "Santiago, Chile - Population 5,000,000"