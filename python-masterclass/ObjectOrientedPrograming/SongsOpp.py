class Song:

    """ This a song class with attributes as below
    Attributes:
        title(str): Name of song
        artist(str): name of the Artist
        duration(int): duration of song can be 0 initially
    """

    def __init__(self, title, artist, duration=0):
        """Initializing the Object with title,artist and duration =0 if not passed"""
        self.title = title
        self.artist = artist
        self.duration = duration

    def get_title(self):
        return self.title

    name = property(get_title)


# help(Song) # gives the doc string

class Album:
    """ Class to represent Album, using its track list
    Attributes:
        name(str): Name of the album
        year(int) : The year Album was released
        artist(str): Name of Artist responsible for album. If not specified shows "Various Artist"
        tracks(List[Song]): A list of songs on the album

    Methods:
        add_song:Used to add new song to the track list
    """

    def __init__(self, name, year, artist=None):
        self.name = name
        self.year = year
        if artist is None:
            self.artist = "Various Artist"
        else:
            self.artist = artist
        self.tracks = []

    def add_song(self, song, position=None):
        """ Add song to the specified position of else add to the end of list"""
        
        song_found = find_item(song, self.tracks)
        if song_found is None:
            song_found = Song(song, self.artist)
            if position is None:
                self.tracks.append(song_found)
            else:
                self.tracks.insert(position, song_found)


class Artist:
    """ Basic class to store artist details
    Attributes:
        name(str): Name of the artist
        albums (List(Album): A list of album by the artist
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

    def add_song(self, name, year, title):
        """ Add new song to collection of album

            New album will be created if does not exists
            name(str): name of album
            year(int): year of song
            title(str): title of the song
        """
        album_found = find_item(name, self.albums)

        if album_found is None:
            print("Album not found")
            album_found = Album(name, year, self.name)
            self.add_album(album_found)
        else:
            print("Album found")

        album_found.add_song(title)


def find_item(field, object_list):
    """ check if filed item is present in the list if not return none """
    for item in object_list:
        if item.name == field:
            return item
    return None


def load_data():
    artist_list = []

    with open('albums.txt', 'r') as albums:
        for line in albums:
            artist_field, album_field, year_field, song_field = tuple(line.strip('\n').split('\t'))
            year_field = int(year_field)
            print("{}:{}:{}:{}".format(artist_field, album_field, year_field, song_field))

            new_artist = find_item(artist_field, artist_list)
            if new_artist is None:
                new_artist = Artist(artist_field)
                artist_list.append(new_artist)

            new_artist.add_song(album_field, year_field, song_field)

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
