import requests
from bs4 import BeautifulSoup
import pandas as pd

def crawl_spotify_viral(url_1):

    response = requests.get(url_1)
    soup = BeautifulSoup(response.content, 'html.parser')
    body = soup.select('tbody')[0]
    chart = pd.DataFrame(columns = ["rank", "song", "artist", "trend"])

    for i in range(10):
        tmp_tag = body.find_all('tr')[i]

        rank = tmp_tag.select('td.chart-table-position')[0].get_text()
        song = tmp_tag.select('td.chart-table-track > strong')[0].get_text()
        artist = tmp_tag.select('td.chart-table-track > span')[0].get_text()[3:]

        if tmp_tag.find('svg')['fill'] == '#84bd00':
            trend = '(UP)'
        elif tmp_tag.find('svg')['fill'] == '#bd3200':
            trend = '(DOWN)'
        elif tmp_tag.find('svg')['fill'] == '#4687d7':
            trend = '(-)'
        elif tmp_tag.find('svg')['fill'] == '#3e3e40':
            trend = '(-)'

        data = {"rank" : rank,
                "song" : song,
                "artist" : artist,
                "trend" : trend,
                }

        chart.loc[len(chart)] = data

    return chart
