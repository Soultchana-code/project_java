from collections import Counter

class StatisticsAnalysis:
    def __init__(self, playlists):
        self.playlists = playlists

    def user_listening_stats(self, user):
        if user in self.playlists:
            all_songs = []
            for playlist in self.playlists[user]:
                all_songs.extend(self.playlists[user][playlist]["songs"])
            song_counts = Counter(all_songs)
            return song_counts.most_common(5)  # Return top 5 most listened songs
        return "User not found."

    def popular_playlists(self):
        playlist_popularity = {}
        for user in self.playlists:
            for playlist in self.playlists[user]:
                playlist_popularity[(user, playlist)] = len(self.playlists[user][playlist]["songs"])
        return sorted(playlist_popularity.items(), key=lambda x: x[1], reverse=True)[:5]  # Top 5 popular playlists