class Song:
    # Class attributes
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}
    
    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        # Add to genres and artists lists (duplicates allowed here)
        Song.genres.append(self.genre)
        Song.artists.append(self.artist)
        # Increment song count
        Song.add_song_to_count()
        # Update genre and artist histograms
        Song.add_to_genres(self.genre)
        Song.add_to_artists(self.artist)
        Song.add_to_genre_count(self.genre)
        Song.add_to_artist_count(self.artist)
    
    @classmethod
    def add_song_to_count(cls):
        cls.count += 1
    
    @classmethod
    def add_to_genres(cls, genre):
        # Only add if genre is not already in the list (control duplicates here)
        if genre not in cls.genres:
            cls.genres.append(genre)
    
    @classmethod
    def add_to_artists(cls, artist):
        # Only add if artist is not already in the list (control duplicates here)
        if artist not in cls.artists:
            cls.artists.append(artist)
    
    @classmethod
    def add_to_genre_count(cls, genre):
        # Update histogram: increment count if genre exists, otherwise initialize to 1
        cls.genre_count[genre] = cls.genre_count.get(genre, 0) + 1
    
    @classmethod
    def add_to_artist_count(cls, artist):
        # Update histogram: increment count if artist exists, otherwise initialize to 1
        cls.artist_count[artist] = cls.artist_count.get(artist, 0) + 1