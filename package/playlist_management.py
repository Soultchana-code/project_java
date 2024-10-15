class PlaylistManagement:
    def __init__(self):
        self.playlists = {}

    def create_playlist(self, user, name, description=""):
        if user not in self.playlists:
            self.playlists[user] = {}
        self.playlists[user][name] = {"description": description, "songs": []}
        return f"Playlist '{name}' created for user {user}."

    def add_song(self, user, playlist, song):
        if user in self.playlists and playlist in self.playlists[user]:
            self.playlists[user][playlist]["songs"].append(song)
            return f"Song '{song}' added to playlist '{playlist}'."
        return "Playlist not found."

    def remove_song(self, user, playlist, song):
        if user in self.playlists and playlist in self.playlists[user]:
            if song in self.playlists[user][playlist]["songs"]:
                self.playlists[user][playlist]["songs"].remove(song)
                return f"Song '{song}' removed from playlist '{playlist}'."
        return "Song or playlist not found."

    def update_playlist_info(self, user, playlist, new_name=None, new_description=None):
        if user in self.playlists and playlist in self.playlists[user]:
            if new_name:
                self.playlists[user][new_name] = self.playlists[user].pop(playlist)
                playlist = new_name
            if new_description:
                self.playlists[user][playlist]["description"] = new_description
            return f"Playlist '{playlist}' updated."
        return "Playlist not found."

    def reorder_songs(self, user, playlist, new_order):
        if user in self.playlists and playlist in self.playlists[user]:
            current_songs = self.playlists[user][playlist]["songs"]
            if set(new_order) == set(current_songs):
                self.playlists[user][playlist]["songs"] = new_order
                return f"Songs in playlist '{playlist}' reordered."
        return "Playlist not found or invalid new order."