class Song:

    """ This a song class with attributes as below
    Attributes:
        title(str): Name of song
        artist(Artist): Artist object for artist details
        duration(int): duration of song can be 0 initially
    """

    def __init__(self, title, artist, duration=0):
        """Initializing the Object with title,artist and duration =0 if not passed"""
        self.title = title
        self.artist = artist
        self.duration = duration


# help(Song) # gives the doc string

class Album:
    """ Class to represent Album, using its track list
    Attributes:
        name(str): Name of the album
        year(int) : The year Album was released
        artist(Artist): Artist responsible for album. If not specified shows "Various Artist"
        tracks(List[Song]): A list of songs on the album

    Methods:
        add_song:Used to add new song to the track list
    """

    def __init__(self, name, year, artist=None):
        self.name = name
        self.year = year
        if artist is None:
            self.artist = Artist("Various Artist")
        else:
            self.artist = artist
        self.tracks = []

    def add_song(self, song, position=None):
        """ Add song to the specified position of else add to the end of list"""

        if position is None:
            self.tracks.append(song)
        else:
            self.tracks.insert(position, song)


class Artist:
    """ Basic class to store artist details
    Attributes:
        name(str): Name of the artist
        albums (List(Album)): A list of album by the artist
    Methods:
        add_album: Use to add album to the albums list
    """

    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album):
        """ Add a new album to the list
        Attributes:
            album(Album) : Album object to be added to the album list
                if Album already present don't add TODO: check to be implemented
        """
        self.albums.append(album)


def find_item(field, object_list):
    """ check if filed item is present in the list if not return none """
    for item in object_list:
        if item.name == field:
            return item
    return None


def load_data():
    new_artist = None
    new_album = None
    artist_list = []

    with open('albums.txt', 'r') as albums:
        for line in albums:
            artist_field, album_field, year_field, song_field = tuple(line.strip('\n').split('\t'))
            year_field = int(year_field)
            print("{}:{}:{}:{}".format(artist_field, album_field, year_field, song_field))

            if new_artist is None:
                new_artist = Artist(artist_field)
                artist_list.append(new_artist)
            elif new_artist.name != artist_field:
                # that means we have found new artist in the data
                # retrieve current artist or create and add the album to it
                new_artist= find_item(artist_field, artist_list)
                if new_artist is None:
                    new_artist = Artist(artist_field)
                    artist_list.append(new_artist)  # add the new artist to artist list

                # new_artist = Artist(artist_field)  # create new artist object
                new_album = None  # its album is None currently

            if new_album is None:
                new_album = Album(album_field, year_field, new_artist)
            elif new_album.name != album_field:
                # we have found new album for this artist
                # store current album in current artist and create new album object
                new_artist.add_album(new_album)
                new_album = Album(album_field, year_field, new_artist)

            # create a new Song object and add it to the album
            song = Song(song_field, new_artist)
            new_album.add_song(song)

        # after last line has been read we need to store the artist and the album
        if new_artist is not None:
            if new_album is not None:
                new_artist.add_album(new_album)
            artist_list.append(new_artist)

    return artist_list


def check_file(artist_list):
    with open('check_file.txt', 'w') as file_to_check:
        for new_artist in artist_list:
            for new_album in new_artist.albums:
                for new_song in new_album.tracks:
                    print("{0.name}\t{1.name}\t{1.year}\t{2.title}".format(new_artist, new_album, new_song),
                          file=file_to_check)


if __name__ == '__main__':
    # load_data()
    artists = load_data()
    print('There are {} artists'.format(len(artists)))

    check_file(artists)
