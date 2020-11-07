import json
from bs4 import BeautifulSoup as bs, FeatureNotFound
import requests
    
url = 'https://alaatv.com/set/963'
req = requests.get(url).content

try :
	soup = bs(req, 'lxml')
except FeatureNotFound :
	soup = bs(req, 'html.parser')

for link in soup.find_all('script', type='application/ld+json'):
	data_dict = json.loads(link.string)
	items = data_dict.get('itemListElement', [])
	for item in items:
		print(item.get('url', ''))

