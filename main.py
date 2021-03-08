import requests
from bs4 import BeautifulSoup

url = requests.get('https://www.detik.com/terpopuler', params={'tag_from': 'wp_cb_mostPopular_more'})

soup = BeautifulSoup(url.text, 'html.parser')

area_popular = soup.find(attrs={'class':'grid-row list-content'})

titles = area_popular.findAll(attrs={'class':'media__title'})
images = area_popular.findAll(attrs={'class':'media__image'})

for image in images:
    print(image.find('a').find('img')['title'])
#print(titles)
