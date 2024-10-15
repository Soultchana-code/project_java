class SharingCollaboration:
    def __init__(self, playlists):
        self.playlists = playlists

    def share_playlist(self, owner, playlist_name, shared_with):
        if owner in self.playlists and playlist_name in self.playlists[owner]:
            if "shared_with" not in self.playlists[owner][playlist_name]:
                self.playlists[owner][playlist_name]["shared_with"] = []
            self.playlists[owner][playlist_name]["shared_with"].append(shared_with)
            return f"Playlist '{playlist_name}' shared with {shared_with}."
        return "Playlist not found."

    def make_collaborative(self, owner, playlist_name):
        if owner in self.playlists and playlist_name in self.playlists[owner]:
            self.playlists[owner][playlist_name]["collaborative"] = True
            return f"Playlist '{playlist_name}' is now collaborative."
        return "Playlist not found."

    def add_collaborator(self, owner, playlist_name, collaborator):
        if owner in self.playlists and playlist_name in self.playlists[owner]:
            if self.playlists[owner][playlist_name].get("collaborative", False):
                if "collaborators" not in self.playlists[owner][playlist_name]:
                    self.playlists[owner][playlist_name]["collaborators"] = []
                self.playlists[owner][playlist_name]["collaborators"].append(collaborator)
                return f"{collaborator} added as collaborator to '{playlist_name}'."
            return "This playlist is not collaborative."
        return "Playlist not found."