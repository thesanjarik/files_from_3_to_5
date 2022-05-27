import requests
from bs4 import BeautifulSoup


URL = 'https://rezka.ag/'

HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36"
}


def get_html(url, params=''):
    req = requests.get(url, headers=HEADERS, params=params)
    return req


def get_data(html):
    soup = BeautifulSoup(html, "html.parser")
    items = soup.find_all('a', class_='b-content__inline_item-link')
    news = []
    for item in items:
        news.append({
            'title': item.find("h2", class_='b-content__inline_item-title').getText(),
            'desc': item.find("p").getText(),
            'link': f"https://rezka.ag/{item.get('href')}",
            'time': item.find("time").getText()
        })
    return news


def parser():
    html = get_html(URL)
    if html.status_code == 200:
       news = []
       for page in range(1, 2):
           html = get_html(f"(URL)page_{page}.php")
           news.extend(get_data(html.text))
       return news
    else:
        raise Exception("ERROR in Parser!")


parser()
