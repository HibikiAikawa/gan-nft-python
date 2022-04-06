from flask import Flask, g, request 
from flask_cors import CORS

import numpy as np
import json   

from createImage import createSvg
from model import imageNet

dbpath = 'test.db' #テーブルを保存するファイル
app = Flask(__name__)
CORS(
    app,
    supports_credentials=True
)

output = './data/output.svg'
width = 16
height = 16
channel = 3


@app.route('/get-image', methods=['GET'])
def get_tweet():
    model = imageNet(width*height*channel)
    seed = np.random.random((1,1))
    pixels = model(seed)
    pixels = pixels.squeeze().cpu().detach().numpy().reshape((width*height, channel)).astype(np.int64)

    createSvg(pixels, output)    
    print('image have created.')
    with open(output, 'r') as f:
        img_code = f.read()
    print('image: ', img_code)
    tweets = []
    tweets.append({"id": 0, "img": img_code})

    return json.dumps(tweets,indent=2)


if __name__ == "__main__":
    app.run() 