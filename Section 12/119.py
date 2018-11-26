# from __future__ import print_function     for use in Python 2 for special printing


class Song:
    """ Class to represent a song

    Attributes:
        title (str): The title of the song
        artist (str): The name of the song's creator.
        duration (int): The duration of the song in seconds. May be zero
    """

    def __init__(self, title, artist, duration=0):
        # """Song init method
        #
        # Args:
        #     title (str): Initialises the 'title' attribute
        #     artist (Artist): An artist object representing the songs creator.
        #     duration (Optional[int]): Initial value of the 'duration' attribute.
        #         Will default to zero if not specified.
        # """
        # docstrings can be used to document modules, functions, classes, and methods
        self.title = title
        self.artist = artist
        self.duration = duration

    def get_title(self):        # A getter
        return self.title

    name = property(get_title)


a_string = "This is\na string split\t\tand tabbed"
print(a_string)

raw_string = r"This is\na string split\t\tand tabbed"   # python does not treat the escape characters when using r""
print(raw_string)

b_string = "This is" + chr(10) + "a string split" + chr(9) + chr(9) + "and tabbed"  # if escape characters didn't exist
print(b_string)

# chr(10) would be different on windows: chr(13)

backslash_string = "this is a backslash \followed by some text"     # f has been treated as a control character
print(backslash_string)

backslash_string = "this is a backslash \\followed by some text"    # back slash appears!
print(backslash_string)

# error_string = r"This string ends with a slash\"     # will cause an error, string isn't terminated
# print(error_string)

good_string = r"This string also ends with a slash\\"
print(good_string)

# r"" - raw string literal

# help(Song)            # Displays docstring for all class methods
# help(Song.__init__)
print(Song.__doc__)     # Class docstring
print(Song.__init__.__doc__)    # Song init docstring

Song.__init__.__doc__ = """Song init method

        Args:
            title (str): Initialises the 'title' attribute
            artist (Artist): An artist object representing the songs creator.
            duration (Optional[int]): Initial value of the 'duration' attribute.
                Will default to zero if not specified.
        """

# ^ won't work in Python 2, wouldn't be able to write to __doc__
help(Song)


class Album:
    """ Class to represent an Album, using it's track list

    Attributes:
        name (str): The name of the album
        year (int): The year the album was released
        artist (str): The name of the artist responsible for the album. If not specified,
            the artist will default to an artist with the name "Various Artists".
        tracks (List[Song]): A list of the songs on the album.

    Methods:
        add_song: Used to add a new song to the album's track list.
    """

    def __init__(self, name, year, artist=None):
        self.name = name
        self.year = year
        if artist is None:
            self.artist = "Various Artists"
        else:
            self.artist = artist

        self.tracks = []

    def add_song(self, song, position=None):
        """ Adds a song to the track list

        Args:
            song (Song): The title of a song to add.
            position (Optional[int]): If specified, the song will be added to that position
                in the track list - inserting it between other songs if necessary.
                Otherwise, the song will be added to the end of the list.
        """

        song_found = find_object(song, self.tracks)
        if song_found is None:
            song_found = Song(song, self.artist)
            if position is None:
                self.tracks.append(song_found)
            else:
                self.tracks.insert(position, song_found)


class Artist:
    """ Basic class to store artist details.

    Attributes:
        name (str): The name of the artist.
        albums (List[Album]): A list of the albums by this artist.
            The list includes only those albums in this collection, it is
            not an exhaustive list of the artist's published albums.

    Methods:
        add_album: Use to add a new album to the artist's album list
    """

    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album):
        """ Add a new album to the list.

        Args:
            album (Album): Album object to add to the list.
                If the album is already present, it will not be added again
                (although this is yet to be implemented).
        """

        self.albums.append(album)

    def add_song(self, name, year, title):
        """ Add a new song to the collection of albums

        This method will add the song to an album in the collection.
        A new album will be createdin the collection if it doesn't already exist.

        Args:
            name (str): The name of the album
            year (int): The year the album was produced
            title (str): The title of the song
        """
        album_found = find_object(name, self.albums)
        if album_found is None:
            print(name + " not found")
            album_found = Album(name, year, self.name)
            self.add_album(album_found)
        else:
            print("Found album " + name)

        album_found.add_song(title)


# Circular references like in this case are best avoided. Artist is referencing Album and vice versa.
# this could cause issues with garbage collection, memory allocation and so forth, where the items
# are permanently in memory... Saving becomes an issue too!

# Circular references can be used, BUT should only be used if needed and if you understand what is going on!


def find_object(field, object_list):
    """ Check 'object_list' to see if an object with a 'name' attribute equal to 'field' exists, return if so. """
    for item in object_list:
        if item.name == field:
            return item
    return None


def load_data():

    artist_list = []

    with open("albums.txt", "r") as albums:
        for line in albums:
            # data row should consist of (artist, album, year, song)
            artist_field, album_field, year_field, song_field = tuple(line.strip('\n').split('\t'))
            year_field = int(year_field)
            print("{}:{}:{}:{}".format(artist_field, album_field, year_field, song_field))

            new_artist = find_object(artist_field, artist_list)
            if new_artist is None:
                new_artist = Artist(artist_field)
                artist_list.append(new_artist)

            new_artist.add_song(album_field, year_field, song_field)

    return artist_list


def create_checkfile(artist_list):
    """ Create a check file from the object data for comparison with the original file"""
    with open("checkfile.txt", "w") as checkfile:
        for new_artist in artist_list:
            for new_album in new_artist.albums:
                for new_song in new_album.tracks:
                    print("{0.name}\t{1.name}\t{1.year}\t{2.title}".format(new_artist, new_album, new_song),  # doesn't work in Python 2
                          file= checkfile)


if __name__ == '__main__':
    artists = load_data()
    print("There are {} artists".format(len(artists)))

    create_checkfile(artists)
