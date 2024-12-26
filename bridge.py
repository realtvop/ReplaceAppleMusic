from appscript import app as attach, its
from types import SimpleNamespace

app = attach('Music')
playlists = app.playlists()

def get_song_info(track_name, artist=None):
    try:
        track = app.library_playlists[1].tracks[its.name == track_name and its.artist == artist].first() \
            if artist else app.library_playlists[1].tracks[its.name == track_name].first()
        
        play_count = track.played_count()
        date_added = track.date_added()

        containing_playlists = []

        for playlist in playlists:
            if playlist.tracks[its.persistent_ID == track.persistent_ID()].exists():
                containing_playlists.append(playlist)

        return SimpleNamespace(
            track=track,
            play_count=play_count,
            # date_added=date_added,
            containing_playlists=containing_playlists,
        )

    except Exception as e:
        print(f"Error finding track: {e}")
