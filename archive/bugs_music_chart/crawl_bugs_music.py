import requests, json, time
from bs4 import BeautifulSoup
import pandas as pd


def crawl_bugs_music(url_1):

    response = requests.get(url_1)
    soup = BeautifulSoup(response.content, 'html.parser')
    body = soup.select('#CHARTday table tbody')[0]
    chart = pd.DataFrame(columns = ["ranking", "song", "artist"])
    
    for i in range(0, 5):
    
        tmp_tag = body.find_all('tr')[i]

        rank = tmp_tag.select('td div.ranking strong')[0].get_text()
        song = tmp_tag.select('th p a')[0].get_text()
        artist = tmp_tag.select('td.left p a')[0].get_text()
        
        data = {"ranking" : rank,
                "song" : song,
                "artist" : artist,
               }

        chart.loc[len(chart)] = data

    return chart
