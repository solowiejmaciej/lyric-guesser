from flask import Flask,jsonify
from flask_cors import CORS, cross_origin
import guesser as guesser
import json

app = Flask(__name__)
CORS(app)


@app.route('/')
@app.route('/song')
def song():
    data = guesser.get_lyric()
    return jsonify({
        "songName":data[0],
        "artistName":data[1],
        "lyric":data[2]
    })

@app.route('/name/')
def default_name():
    return jsonify({
        "Error":"Invalid name"
    })
@app.route('/name/<artistName>')
def name(artistName):
    try:
        data = guesser.get_song_by_artist(artistName)
        return jsonify({
            "songName":data[0],
            "artistName":data[1],
            "lyric":data[2]
        })
    except ValueError:
        return jsonify({
        "error":"invalid name"
    })



if __name__ == '__main__':
    app.run(host='127.0.0.1', port=3500)
