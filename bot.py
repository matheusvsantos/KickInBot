from requests import post
import json

def type_url(url):
    try:
        api_url = 'http://url.veleci.bid/'
        data = {
            'url': url
        }
        b_url = post(api_url, data)
        if b_url.status_code is 201:
            return json.loads(b_url.content.decode("utf-8").replace('\n',''))['short_url']
        return url
    except Exception as err:
        return url

def send_Message(last_news, bot, last_data):
    try:
        if last_news is not None and last_news['data'] > last_data:
            last_data = last_news['data']
            short_link = type_url(last_news['link'])
            bot.sendMessage('@KickInBtohers',last_news['title']+"\n"+short_link)
            print(last_news)
            return last_data
        else:
            return last_data
    except Exception as err:
        print(err)
        return last_data
