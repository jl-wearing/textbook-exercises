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


#Process.
while True:
    print("Enter album details, or 'q' to quit: ")
    #Input
    artist_name = input('Artist name: ')
    if artist_name == 'q':
        break

    album_title = input('Artist title: ')
    if album_title == 'q':
        break

    response = input('Do you know the number of tracks in the album? (y/n)?: ')
    if response == 'y':
        number_of_songs = int(input('Enter the number of songs: '))

        #Output
        album = make_album(artist_name, album_title, number_of_songs)
        print(album)
    else:
        album = make_album(artist_name, album_title)
        print(album)