import re
import bs4
import requests


def parse_ym():
    with requests.session() as s:
        resp = s.get('https://market.yandex.ru')
        sk = re.findall(r'"sk":"(y[a-f0-9]+)",', resp.text)[0]
        resp = s.get(
            'https://market.yandex.ru/api/search',
            params=dict(
                how='aprice', hid=91031,
                glfilter='4878792:13866258', onstock=1, sk=sk
            )
        )
        data = resp.json()['data']
        page = bs4.BeautifulSoup(data, 'lxml')
        for pr in page.find_all('div', {'class': 'price'}):
            price = int(re.findall('[0-9]+', pr.text.replace(' ', ''))[0])
            yield price


if __name__ == '__main__':
    for price in parse_ym():
        print(price)
