# -*- coding: utf-8 -*-

from flask import Flask
from flask import request
from flask import jsonify
from flask import json

import requests, time
from bs4 import BeautifulSoup
import pandas as pd

from crawl_spotify_viral import *

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route("/keyboard")
def keyboard():
    return jsonify({
        "type" : "buttons",
        "buttons" : ["Global",
                     "United States",
                     "United Kingdom",
                     "Argentina",
                     "Australia",
                     "Canada",
                     "Brazil",
                     "Chile",
                     "Colombia",
                     "France",
                     "Germany",
                     "Hong Kong",
                     "Japan",
                     "Malaysia",
                     "Mexico",
                     "Singapore",
                     "Spain",
                     "Taiwan"
                    ]
    })


@app.route("/message", methods=["POST"])
def message():
    data = request.get_json()
    content = data["content"]

    if content == "Global":
        text = "Spotify Viral " + str(content)
        url = "https://imgur.com/zs7t25X.png"
        url_1 = "https://spotifycharts.com/viral/global/daily/latest"
        label = "차트 전체순위 보러가기"
        result1 = crawl_spotify_viral(url_1)

    elif content == "United States":
        text = "Spotify Viral " + "US"
        url = "https://imgur.com/zs7t25X.png"
        url_1 = "https://spotifycharts.com/viral/us/daily/latest"
        label = "차트 전체순위 보러가기"
        result1 = crawl_spotify_viral(url_1)

    elif content == "United Kingdom":
        text = "Spotify Viral " + "UK"
        url = "https://imgur.com/zs7t25X.png"
        url_1 = "https://spotifycharts.com/viral/gb/daily/latest"
        label = "차트 전체순위 보러가기"
        result1 = crawl_spotify_viral(url_1)

    elif content == "Argentina":
        text = "Spotify Viral " + str(content)
        url = "https://imgur.com/zs7t25X.png"
        url_1 = "https://spotifycharts.com/viral/ar/daily/latest"
        label = "차트 전체순위 보러가기"
        result1 = crawl_spotify_viral(url_1)

    elif content == "Australia":
        text = "Spotify Viral " + str(content)
        url = "https://imgur.com/zs7t25X.png"
        url_1 = "https://spotifycharts.com/viral/at/daily/latest"
        label = "차트 전체순위 보러가기"
        result1 = crawl_spotify_viral(url_1)


    elif content == "Brazil":
        text = "Spotify Viral " + str(content)
        url = "https://imgur.com/zs7t25X.png"
        url_1 = "https://spotifycharts.com/viral/br/daily/latest"
        label = "차트 전체순위 보러가기"
        result1 = crawl_spotify_viral(url_1)

    elif content == "Canada":
        text = "Spotify Viral " + str(content)
        url = "https://imgur.com/zs7t25X.png"
        url_1 = "https://spotifycharts.com/viral/ca/daily/latest"
        label = "차트 전체순위 보러가기"
        result1 = crawl_spotify_viral(url_1)

    elif content == "Chile":
        text = "Spotify Viral " + str(content)
        url = "https://imgur.com/zs7t25X.png"
        url_1 = "https://spotifycharts.com/viral/cl/daily/latest"
        label = "차트 전체순위 보러가기"
        result1 = crawl_spotify_viral(url_1)

    elif content == "Colombia":
        text = "Spotify Viral " + str(content)
        url = "https://imgur.com/zs7t25X.png"
        url_1 = "https://spotifycharts.com/viral/co/daily/latest"
        label = "차트 전체순위 보러가기"
        result1 = crawl_spotify_viral(url_1)

    elif content == "France":
        text = "Spotify Viral " + str(content)
        url = "https://imgur.com/zs7t25X.png"
        url_1 = "https://spotifycharts.com/viral/fr/daily/latest"
        label = "차트 전체순위 보러가기"
        result1 = crawl_spotify_viral(url_1)

    elif content == "Germany":
        text = "Spotify Viral " + str(content)
        url = "https://imgur.com/zs7t25X.png"
        url_1 = "https://spotifycharts.com/viral/de/daily/latest"
        label = "차트 전체순위 보러가기"
        result1 = crawl_spotify_viral(url_1)

    elif content == "Hong Kong":
        text = "Spotify Viral " + str(content)
        url = "https://imgur.com/zs7t25X.png"
        url_1 = "https://spotifycharts.com/viral/hk/daily/latest"
        label = "차트 전체순위 보러가기"
        result1 = crawl_spotify_viral(url_1)

    elif content == "Japan":
        text = "Spotify Viral " + str(content)
        url = "https://imgur.com/zs7t25X.png"
        url_1 = "https://spotifycharts.com/viral/jp/daily/latest"
        label = "차트 전체순위 보러가기"
        result1 = crawl_spotify_viral(url_1)

    elif content == "Malaysia":
        text = "Spotify Viral " + str(content)
        url = "https://imgur.com/zs7t25X.png"
        url_1 = "https://spotifycharts.com/viral/my/daily/latest"
        label = "차트 전체순위 보러가기"
        result1 = crawl_spotify_viral(url_1)

    elif content == "Mexico":
        text = "Spotify Viral " + str(content)
        url = "https://imgur.com/zs7t25X.png"
        url_1 = "https://spotifycharts.com/viral/mx/daily/latest"
        label = "차트 전체순위 보러가기"
        result1 = crawl_spotify_viral(url_1)

    elif content == "Singapore":
        text = "Spotify Viral " + str(content)
        url = "https://imgur.com/zs7t25X.png"
        url_1 = "https://spotifycharts.com/viral/sg/daily/latest"
        label = "차트 전체순위 보러가기"
        result1 = crawl_spotify_viral(url_1)

    elif content == "Spain":
        text = "Spotify Viral " + str(content)
        url = "https://imgur.com/zs7t25X.png"
        url_1 = "https://spotifycharts.com/viral/es/daily/latest"
        label = "차트 전체순위 보러가기"
        result1 = crawl_spotify_viral(url_1)

    elif content == "Taiwan":
        text = "Spotify Viral " + str(content)
        url = "https://imgur.com/zs7t25X.png"
        url_1 = "https://spotifycharts.com/viral/tw/daily/latest"
        label = "차트 전체순위 보러가기"
        result1 = crawl_spotify_viral(url_1)


    # response
    response = {
      "message": {
        "text": text + "\n\n" +
                str(result1.loc[0, 'rank']) + "위 : " + str(result1.loc[0, 'song']) + " - " + str(result1.loc[0, 'artist']) + "\n" +
                str(result1.loc[1, 'rank']) + "위 : " + str(result1.loc[1, 'song']) + " - " + str(result1.loc[1, 'artist']) + "\n" +
                str(result1.loc[2, 'rank']) + "위 : " + str(result1.loc[2, 'song']) + " - " + str(result1.loc[2, 'artist']) + "\n" +
                str(result1.loc[3, 'rank']) + "위 : " + str(result1.loc[3, 'song']) + " - " + str(result1.loc[3, 'artist']) + "\n" +
                str(result1.loc[4, 'rank']) + "위 : " + str(result1.loc[4, 'song']) + " - " + str(result1.loc[4, 'artist']) + "\n" +
                str(result1.loc[5, 'rank']) + "위 : " + str(result1.loc[5, 'song']) + " - " + str(result1.loc[5, 'artist']) + "\n" +
                str(result1.loc[6, 'rank']) + "위 : " + str(result1.loc[6, 'song']) + " - " + str(result1.loc[6, 'artist']) + "\n" +
                str(result1.loc[7, 'rank']) + "위 : " + str(result1.loc[7, 'song']) + " - " + str(result1.loc[7, 'artist']) + "\n" +
                str(result1.loc[8, 'rank']) + "위 : " + str(result1.loc[8, 'song']) + " - " + str(result1.loc[8, 'artist']) + "\n" +
                str(result1.loc[9, 'rank']) + "위 : " + str(result1.loc[9, 'song']) + " - " + str(result1.loc[9, 'artist']) + "\n",

        # return image
        "photo": {
          "url": url,
          "width": 640,
          "height": 480
        },

        # message button
        "message_button": {
          "label": label,
          "url": url_1
        }
      },


      "keyboard": {
        "type": "buttons",
        "buttons" : ["Global",
                     "United States",
                     "United Kingdom",
                     "Argentina",
                     "Australia",
                     "Canada",
                     "Brazil",
                     "Chile",
                     "Colombia",
                     "France",
                     "Germany",
                     "Hong Kong",
                     "Japan",
                     "Malaysia",
                     "Mexico",
                     "Singapore",
                     "Spain",
                     "Taiwan"
                    ]
      }
    }

    response = json.dumps(response, ensure_ascii=False)
    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
