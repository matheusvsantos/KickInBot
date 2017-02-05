from requests import get, post
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import feedparser
from dateutil.parser import parse
import datetime

def save_api(last_news, fonte):
    json_data = {
        'link': last_news['link'],
        'title': last_news['title'],
        'data': str(last_news['data']),
        'fonte': fonte
    }
    request = post('http://peladobrothers.herokuapp.com/api/noticias/', json_data)
    if request.status_code is 400:
        return False
    if request.status_code is 201:
        return True
    return None

def espn_parse(url):
    try:
        espn_html = BeautifulSoup(get(url).content, 'html.parser')
        card = espn_html.find_all(attrs={'class':'card'})[0]
        last_data_espn = parse(card.h4.text)
        url_base = 'http://espn.uol.com.br/'
        last_news_espn = { 'link': urljoin(url_base,card.a.get('href')), 'title': card.a.get('title'), 'data': last_data_espn }
        if save_api(last_news_espn,'ESPN') is True:
            return last_news_espn
        else:
            return None
        return last_news_espn
    except Exception as e:
        return None

def rss_parse(url, fonte):
    try:
        feed = feedparser.parse(url)['entries'][0]
        if 'T' in feed['published']:
            last_data = parse(feed['published'].replace('T',' ').replace('Z',''))
        else:
            last_data = parse(feed['published'][::-1][4:][::-1])
        last_news = { 'link': feed['link'], 'title' : feed['title'], 'data': last_data }
        if save_api(last_news, fonte) is True:
            return last_news
        else:
            return None
        return last_news
    except Exception as e:
        return None
