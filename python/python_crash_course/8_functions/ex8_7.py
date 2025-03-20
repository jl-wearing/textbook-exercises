#Write a function that builds a dictionary describing an album.

def make_album(artist_name, album_title, number_of_songs=None):
    """Dictionary of information about a music album."""
    if number_of_songs:
        album = {
            'artist': artist_name.title(),
            'title': album_title.title(),
            'number of tracks': number_of_songs,
        }
    else:
        album = {
            'artist': artist_name.title(),
            'title': album_title.title(),
        }

    return album

#Testing the function.
album_1 = make_album('chris brown', 'some album', 22)
album_2 = make_album('lil wayne', "i don't know")

#Output
print(album_1)
print(album_2)