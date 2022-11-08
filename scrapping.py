from asyncio.windows_events import NULL
from lyricsgenius import Genius
TOKEN = "JNMe1zq_JLms6G2TzLtSbajwl8ICDCFsgVla45b8VqVpZJd8493Km1UlHJ_wLW7G"


def get_lyrics(artistName,songName):
    genius = Genius(TOKEN)
    genius.verbose = False
    genius.remove_section_headers = True
    artist = genius.search_artist(artistName, max_songs=0)
    song = artist.song(songName)
    #'NoneType' object has no attribute 'song'
    try: 
        lyric = song.lyrics
    except AttributeError:
        lyric = NULL
    return lyric

