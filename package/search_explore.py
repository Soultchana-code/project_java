class SearchExplore:
    def __init__(self, playlists):
        self.playlists = playlists

    def search_songs(self, query):
        results = []
        for user in self.playlists:
            for playlist in self.playlists[user]:
                for song in self.playlists[user][playlist]["songs"]:
                    if query.lower() in song.lower():
                        results.append(song)
        return results

    def explore_public_playlists(self):
        public_playlists = []
        for user in self.playlists:
            for playlist in self.playlists[user]:
                if self.playlists[user][playlist].get("public", False):
                    public_playlists.append((user, playlist))
        return public_playlists

    def recommend_songs(self, user):
        # This is a simple recommendation system. In a real-world scenario, 
        # you'd use more sophisticated algorithms.
        all_songs = set()
        user_songs = set()
        for u in self.playlists:
            for playlist in self.playlists[u]:
                if u == user:
                    user_songs.update(self.playlists[u][playlist]["songs"])
                all_songs.update(self.playlists[u][playlist]["songs"])
        
        recommendations = list(all_songs - user_songs)
        return recommendations[:5]  # Return top 5 recommendations