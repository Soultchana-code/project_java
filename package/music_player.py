class MusicPlayer:
    def __init__(self):
        self.current_playlist = []
        self.current_song_index = -1
        self.is_playing = False

    def load_playlist(self, playlist):
        self.current_playlist = playlist
        self.current_song_index = 0

    def play(self):
        if self.current_playlist:
            self.is_playing = True
            return f"Playing: {self.current_playlist[self.current_song_index]}"
        return "No playlist loaded."

    def pause(self):
        if self.is_playing:
            self.is_playing = False
            return "Paused."
        return "Not playing."

    def next_song(self):
        if self.current_playlist:
            self.current_song_index = (self.current_song_index + 1) % len(self.current_playlist)
            return self.play()
        return "No playlist loaded."

    def previous_song(self):
        if self.current_playlist:
            self.current_song_index = (self.current_song_index - 1) % len(self.current_playlist)
            return self.play()
        return "No playlist loaded."