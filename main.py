import requests
from bs4 import BeautifulSoup as bs
import time

HOME_URL = 'https://stei.itb.ac.id/'
DOMAIN = 'stei.itb.ac.id'
URL_LIST = []

def is_in_domain(link,domain=DOMAIN):
    if DOMAIN in link:
        return True
    else: return False

def is_file(link):
    if '.' in link.split('/')[-1]:
        #print(link.split('/')[-1])
        return True
    else: return False
    
def scrape_stei(f, url = HOME_URL):
    #print(f'\033[F{url}',end='')
    if is_in_domain(url):
        print(url)
        try:
            html = requests.get(url).content
            soup = bs(html,'html.parser')
            home_soup = soup.find_all('a')
            for a in home_soup:
                link = a.get('href')
                if is_in_domain(link,DOMAIN):
                    if link not in URL_LIST:
                        URL_LIST.append(link)
                        if is_file(link):
                            print(link)
                            f.write(link)
                        scrape_stei(f,url=link)
                    else:continue
        except:pass

if __name__ == '__main__':
    with open('scrape-stei.log','a') as f:
        scrape_stei(f,HOME_URL)
