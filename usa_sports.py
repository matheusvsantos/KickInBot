from dateutil.parser import parse
import telepot
import time
from bot import send_Message
from parses import espn_parse, rss_parse

def follow_us_sports():
    bot = telepot.Bot('311828222:AAGCcuZSwRoyrcfOTwZoTaPD3xwBlmlq6ZI')
    dates = {
        'espn_nba': parse('01/01/2016'),
        'espn_nfl': parse('01/01/2016'),
        'espnbr_nba': parse('01/01/2016'),
        'espnbr_nfl': parse('01/01/2016'),
        'nba': parse('01/01/2016'),
        'nfl': parse('01/01/2016'),
        'cbs': parse('01/01/2016')
    }
    url_rss = {
        'nfl': 'http://www.nfl.com/rss/rsslanding?searchString=home',
        'cbs': 'http://rss.cbssports.com/rss/headlines',
        'espn_nba': 'http://www.espn.com/espn/rss/nba/news',
        'espn_nfl': 'http://www.espn.com/espn/rss/nfl/news',
        'nba': 'http://www.nba.com/rss/nba_rss.xml',
        'espnbr_nfl': 'http://espn.uol.com.br/modalidade/nfl',
        'espnbr_nba': 'http://espn.uol.com.br/modalidade/nba'
    }
    while(1):
        try:
            for key, values in url_rss.items():
                if key is 'espnbr_nfl' or key is 'espnbr_nba':
                    dates[key] = send_Message(espn_parse(values), bot, dates[key])
                else:
                    dates[key] = send_Message(rss_parse(values, key), bot, dates[key])
        except Exception as err:
            time.sleep(15)

follow_us_sports()
