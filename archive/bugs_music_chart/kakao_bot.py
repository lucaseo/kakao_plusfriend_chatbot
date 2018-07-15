# -*- coding: utf-8 -*-

from flask import Flask
from flask import request
from flask import jsonify
from flask import json

import requests, json, time
from bs4 import BeautifulSoup
import pandas as pd

from crawl_bugs_music import *

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route("/keyboard")
def keyboard():
    response = {
        "type" : "buttons",
        "buttons" : ["해외 - 랩/힙합",
                     "해외 - 알앤비/소울",
                     "해외 - 팝",
                     "국내 - 랩/힙합",
                     "국내 - 알앤비/소울",
                     "국내 - 댄스/팝/발라드",
                     ]
    }
    response = json.dumps(response, ensure_ascii=False)
    return response


@app.route("/message", methods=["POST"])
def message():
    data = json.loads(request.data)
    content = data["content"]

    if content == "해외 - 랩/힙합":
        text = "이번 주 [해외 - 랩/힙합] 순위입니다."
        url = "https://imgur.com/oqYER0L.jpg"
        url_1 = "https://music.bugs.co.kr/chart/track/day/nfhiphop"
        label = "[해외 - 랩/힙합] 전체순위 보러가기"
        result1 = crawl_bugs_music(url_1)

    elif content == "해외 - 알앤비/소울":
        text = "이번 주 [해외 - 알앤비/소울] 순위입니다."
        url = "https://imgur.com/oqYER0L.jpg"
        url_1 = "https://music.bugs.co.kr/chart/track/day/nfrnb"
        label = "[해외 - 알앤비/소울] 전체순위 보러가기"
        result1 = crawl_bugs_music(url_1)

    elif content == "해외 - 팝":
        text = "이번 주 [해외 - 알앤비/소울] 순위입니다."
        url = "https://imgur.com/oqYER0L.jpg"
        url_1 = "https://music.bugs.co.kr/chart/track/day/nfpop"
        label = "[해외 - 팝] 전체순위 보러가기"
        result1 = crawl_bugs_music(url_1)


    elif content == "국내 - 랩/힙합":
        text = "이번 주 [국내 - 랩/힙합] 순위입니다."
        url = "https://imgur.com/oqYER0L.jpg"
        url_1 = "https://music.bugs.co.kr/chart/track/day/nrh"
        label = "[국내 - 랩/힙합] 전체순위 보러가기"
        result1 = crawl_bugs_music(url_1)


    elif content == "국내 - 알앤비/소울":
        text = "이번 주 [국내 - 알앤비/소울] 순위입니다."
        url = "https://imgur.com/oqYER0L.jpg"
        url_1 = "https://music.bugs.co.kr/chart/track/day/nrs"
        label = "[국내 - 알앤비/소울] 전체순위 보러가기"
        result1 = crawl_bugs_music(url_1)

    elif content == "국내 - 댄스/팝/발라드":
        text = "이번 주 [국내 - 알앤비/소울] 순위입니다."
        url = "https://imgur.com/oqYER0L.jpg"
        url_1 = "https://music.bugs.co.kr/chart/track/day/nbdp"
        label = "[국내 - 댄스/팝/발라드] 전체순위 보러가기"
        result1 = crawl_bugs_music(url_1)


    # response
    response = {
      "message": {
        "text": text + "\n" +
                str(result1.loc[0, 'ranking']) + "위 : " + str(result1.loc[0, 'song']) + " - " + str(result1.loc[0, 'artist']) + "\n" +
                str(result1.loc[1, 'ranking']) + "위 : " + str(result1.loc[1, 'song']) + " - " + str(result1.loc[1, 'artist']) + "\n" +
                str(result1.loc[2, 'ranking']) + "위 : " + str(result1.loc[2, 'song']) + " - " + str(result1.loc[2, 'artist']) + "\n" +
                str(result1.loc[3, 'ranking']) + "위 : " + str(result1.loc[3, 'song']) + " - " + str(result1.loc[3, 'artist']) + "\n" +
                str(result1.loc[4, 'ranking']) + "위 : " + str(result1.loc[4, 'song']) + " - " + str(result1.loc[4, 'artist']) + "\n",

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
        "buttons": ["해외 - 랩/힙합",
                    "해외 - 알앤비/소울",
                    "해외 - 팝",
                    "국내 - 랩/힙합",
                    "국내 - 알앤비/소울",
                    "국내 - 댄스/팝/발라드",
                     ]
      }
    }

    response = json.dumps(response, ensure_ascii=False)
    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
