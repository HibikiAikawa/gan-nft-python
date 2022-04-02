from flask import Flask, g, request 
from flask_cors import CORS

import sqlite3
import json   

from create_image import create_image

dbpath = 'test.db' #テーブルを保存するファイル
app = Flask(__name__)
CORS(
    app,
    supports_credentials=True
)


@app.route('/get-image', methods=['GET'])
def get_tweet():
    img = create_image()
    print('image have created.')
    tweets = []
    tweets.append({"id": 0, "img": img.decode('utf-8')})

    return json.dumps(tweets,indent=2)


if __name__ == "__main__":
    app.run() 