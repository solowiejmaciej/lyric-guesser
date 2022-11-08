import pandas as pd
import scrapping
import db_connect
from langdetect import detect

db = db_connect.db
cursor = db.cursor()
for l in range(1,46):
    fileName= "data " +"("+str(l)+")"
    file= pd.read_csv('./data/' + fileName +'.csv')
    artists = file.artist_names
    songs = file.track_name
    uri = file.uri
    #print(scrapping.get_lyrics(artists[0], songs[0]))
    for x in range(len(songs)):
        currentArtist = artists[x]
        currentSong = songs[x]
        currentUri = uri[x]
        cursor.execute("select songName from songs where songName =%s", (currentSong,))
        record = cursor.fetchall()
        try:
            if record[0][0] == currentSong:
                print("Already in db")
        except IndexError:
            lyric = scrapping.get_lyrics(currentArtist.split(',')[0],currentSong) 
            result_lyric = lyric
            if lyric==0 or int(lyric.count('-'))>int(len(lyric.split('\n'))-20):
                result_lyric=0
                lyric=0
                print("Unable to fetch lyrics or lyrics is wrong")
            else:
                try:
                    lyric_list = lyric.split('\n')
                    lyric_list.remove("You might also like")
                    lyric_list = list(filter(None, lyric_list))
                    result_lyric = '\n'.join(lyric_list)
                except ValueError:
                    pass
            try: 
                lang = str(detect(lyric))
            except Exception:
                lang = None
            cursor.execute("INSERT INTO songs (artistName,songName,lyric,uri,lang) VALUES(%s,%s,%s,%s,%s)",(currentArtist, currentSong,result_lyric,currentUri,lang))
            db.commit()
            print(currentSong +" by " + currentArtist + " inserted into db")
    print(l)
#cursor.execute("INSERT INTO songs (artistName,songName,lyric) VALUES(%s,%s,%s)",("żęgorzłóćą","żęgorzłóćą","żęgorzłóćą"))

