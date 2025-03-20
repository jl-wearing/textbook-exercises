#Program to create a dictionary of an album.

def make_album(album_title, artist_name, number_of_tracks=None, year_of_release=None):
    """Create a collection describing a musician's album."""
    album = {'title': album_title, 'author': artist_name}

    if number_of_tracks:
        album['number of songs'] = number_of_tracks

    if year_of_release:
        album['year'] = year_of_release

    return album

#Testing the make_album() function.
avicii = make_album('true', 'avicii', year_of_release=2013)
for key, value in avicii.items():
    if key != 'year':
        print(f"{key.title()}: {value.title()}")
    else:
        print(f"{key.title()}: {value}")
print()