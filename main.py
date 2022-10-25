import requests
from bs4 import BeautifulSoup as bs
import time

HOME_URL = 'https://stei.itb.ac.id/'
DOMAIN = 'stei.itb.ac.id'
GREAT_LIST = []

def in_domain(link,domain=DOMAIN):
    try:
        if DOMAIN in link.split('/')[2]:
            #print(f'{link} is inside of {DOMAIN}.')
            return True
        else: 
            #print(f'{link} is out of {DOMAIN}.')
            return False
    except: return False

def is_file(link):
    if '.' in link.split('/')[-1]:
        return True
    else: return False

def has_href(a):
    try:
        return a['href']
    except: return None

def get_children(f,url):
    children = {}
    children[DOMAIN] = []
    html = requests.get(url).content
    soup = bs(html,'html.parser')
    a_soup = soup.find_all('a')
    for a in a_soup:
        try:
            a_href = has_href(a)
            if a_href.startswith('#'):
                continue
            elif a_href.startswith('/'):
                a_href = 'https://'+DOMAIN+a_href
                children[DOMAIN].append(a_href)
            elif in_domain(a_href,DOMAIN):
                if a_href != url and a_href not in GREAT_LIST:
                    f.write(a_href+'\n')
                    GREAT_LIST.append(a_href)    
                    print(url, a_href)
                    get_children(f,a_href)
   
        except:continue
    #input()
    print(f'Parent: {url}')
    for child in children[DOMAIN]:
        print(f'\t{child}')
    return children[DOMAIN]
    
def scrape2(f, url=HOME_URL):
    get_children(f,url)
        
    
if __name__ == '__main__':
    with open('scrape-stei.log','a') as f:
        scrape2(f, HOME_URL)
