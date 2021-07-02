from bs4 import BeautifulSoup
import requests

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) \
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}

def fetch_proxy():
    source = requests.get('https://free-proxy-list.net/', headers=headers)
    soup = BeautifulSoup(source.text, 'lxml')
    proxies = []
    table = soup.find('tbody')
    rows = table.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        proxy = '{}:{}'.format(cols[0].text, cols[1].text)
        proxies.append(proxy)
    return proxies

def test_url(proxy):
    try:
        source = requests.get(URL, headers=headers,
                              proxies={'http': proxy, 'https': proxy}, timeout=1)
        if source.status_code == 200:
            print(f'{proxy} works')
            return True
    except:
        pass

URL = ''
proxies = fetch_proxy()
available_proxies = []
for proxy in proxies:
    if test_url(proxy):
        available_proxies.append(proxy)

