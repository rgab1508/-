import requests
from bs4 import BeautifulSoup

def crawl_man(url):
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, 'html.parser')
    print(plain_text)

    for div in soup.findAll('div', {'class': 'floatnone'}):
        print(div)
        for img in div.findAll('img'):
            print(img)
            src = img.get('data-original')
            print(src)
            

crawl_man("http://youtube.com")



