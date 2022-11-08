import db_connect
import random


db = db_connect.db
cursor = db.cursor()


def get_random_id():
    ids=[]
    cursor.execute("SELECT * FROM songs WHERE lyric <> '0' AND lang='pl'")
    results = cursor.fetchall()
    for x in range(len(results)):
        ids.append(results[x][0])
    random_id=ids[random.randint(1,len(ids)-1)]
    return random_id

def get_song_data():
    random_id = get_random_id()
    cursor.execute("select songName,artistName,lyric from songs where id =%s", (random_id,))
    result = cursor.fetchone()
    return result


def get_lyric():
    row_number = 8
    song = get_song_data()
    songName = song[0]
    artistName = song[1]
    lyric = song[2]

    formated_lyric = lyric.split('\n') #towrszymy liste z tekstem piosenki kazdy elementy listy to tekst do pierwszgo entera
    picked_lyric = []
    guess_data = []
    start_value = random.randint(3,int(len(formated_lyric)-12)) #bierzemy srodek piosenki zeby bylo troche latwiej
    end_value = start_value+row_number #row number to ilosc wierszow ktore chcemy miec

    for x in range(start_value, end_value):
        picked_lyric.append(formated_lyric[x])

    guess_data.append(songName)
    guess_data.append(artistName)
    guess_data.append(picked_lyric)
    return guess_data

def get_song_by_artist(artistName):
    ids=[]
    cursor.execute("SELECT * FROM songs WHERE lyric <> '0' AND lang='pl' and artistName LIKE %s",("%"+artistName+"%",))
    results = cursor.fetchall()
    for x in range(len(results)):
        ids.append(results[x][0])
    random_id=ids[random.randint(1,len(ids)-1)]
    cursor.execute("select songName,artistName,lyric from songs where id =%s", (random_id,))
    song = cursor.fetchone()
    songName = song[0]
    artistName = song[1]
    lyric = song[2]
    row_number = 8
    formated_lyric = lyric.split('\n') #towrszymy liste z tekstem piosenki kazdy elementy listy to tekst do pierwszgo entera
    picked_lyric = []
    guess_data = []
    start_value = random.randint(3,int(len(formated_lyric)-12)) #bierzemy srodek piosenki zeby bylo troche latwiej
    end_value = start_value+row_number #row number to ilosc wierszow ktore chcemy miec
    for x in range(start_value, end_value):
        picked_lyric.append(formated_lyric[x])

    guess_data.append(songName)
    guess_data.append(artistName)
    guess_data.append(picked_lyric)
    return guess_data