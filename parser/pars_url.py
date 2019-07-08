import requests
from bs4 import BeautifulSoup
import csv

def get_html(url):
    r=requests.get(url)
    return r.text


def get_total_pages(html):#кол-во страниц
    soup=BeautifulSoup(html,'lxml')
    pages=soup.find('div',class_='pagination-pages clearfix').find_all('a',class_='pagination-page')[-1].get('href')
    total_pages=pages.split('=')[1].split('&')[0]
    return int(total_pages)

def get_page_data(html):
    soup=BeautifulSoup(html,'lxml')
    ads=soup.find('div',class_='catalog-list js-catalog-list clearfix').find_all('a',class_='item-description-title-link').get('href')
    print(ads)
    return ads




def main():
    url='https://www.avito.ru/irkutsk/avtomobili?p=1&radius=300'
    base_url='https://www.avito.ru/irkutsk/avtomobili?'
    page_part='p='
    query_part='&radius=300'
    total_pages=get_total_pages(get_html(url))
    for i in range(1,total_pages):
        url_gen=base_url+page_part+str(i)+query_part
        with open('AUTO_HREF.csv', 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(([url_gen]))
            print(([url_gen]))





if __name__ == '__main__':
    main()
