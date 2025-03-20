from name_function import get_formatted_name

def test_first_last_name():
    """Do names like Janis Joplin work?"""
    full_name = get_formatted_name('janis', 'joplin')
    assert full_name == "Janis Joplin"

def test_first_last_middle_name():
    """Do names like Wolfgang Amadeus Mozart work?"""
    full_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
    assert full_name == "Wolfgang Amadeus Mozart"
