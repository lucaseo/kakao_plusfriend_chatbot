import requests, json, time
from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd


def crawl_naver_music(url_1):

    html = urlopen(url_1)
    soup = BeautifulSoup(html, 'html.parser')
    body = soup.select('tbody tr')[1:6]
    melon_genre = pd.DataFrame(columns = ["Ranking", "Song", "Artist"])

    for i in range(0, 5):

        tmp_tag = body[i]

        rank = tmp_tag.select('td.ranking')[0].get_text()
        song = tmp_tag.select('td a._title .ellipsis')[0].get_text()
        try:
            artist = tmp_tag.select('td a._artist .ellipsis')[0].get_text()
            artist = artist[15:-4]
        except IndexError:
            artist = tmp_tag.select('td._artist.artist.no_ell2 > a')[0].get_text()



        data = {"Ranking" : rank,
                "Song" : song,
                "Artist" : artist,
               }

        melon_genre.loc[len(melon_genre)] = data


    return melon_genre
