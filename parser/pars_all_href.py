import requests
from bs4 import BeautifulSoup
import csv
import certifi
from time import sleep


def get_html(url):
    r=requests.get(url.strip(),verify=certifi.where())
    return r.text
def get_all_links(html):
    soup=BeautifulSoup(html,'lxml')
    tables=soup.find('div',class_='catalog-list js-catalog-list clearfix').find_all('h3',class_='title item-description-title')
    links=[]
    for table in tables:
        a_bes_https=table.find('a').get('href')
        a='https://www.avito.ru/'+a_bes_https
        links.append(a)
    print(links)

    #links_postrochno=('\n'.join(links))
    #print(links_postrochno)

    return links


def write_csv(links):
    with open('all_links.csv','a') as file:
        writer=csv.writer(file)
        for item in links:
            writer.writerow([item])


def main():
    with open('AUTO_HREF.csv', 'r') as f:
        reader = csv.reader(f)
        your_list = list(reader)
    new_list = []
    for sub_list in your_list:
        for el in sub_list:
            new_list.append(el)
    zzz = 0
    for i in range(len(new_list)):
        url = new_list[zzz]
        zzz += 1
        sleep(2)

        write_csv(get_all_links(get_html(url)))

if __name__ == '__main__':
    main()