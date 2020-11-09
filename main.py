#load libraries 
import json
from bs4 import BeautifulSoup as bs, FeatureNotFound
import requests

    
url = 'https://alaatv.com/set/963'
req = requests.get(url).content
links = []
download_links = []

try :
	soup = bs(req, 'lxml')
except FeatureNotFound :
	soup = bs(req, 'html.parser')

for link in soup.find_all('script', type='application/ld+json'):
	data_dict = json.loads(link.string)
	items = data_dict.get('itemListElement', [])
	for item in items:
		links.append(item.get('url', ''))
		


for i in links:

	request = requests.get(i).content
	soup_ = bs(request, 'html.parser') 
	source = soup_.find_all('source')
	srcs = [link['src'] for link in source if 'src' in link.attrs]
	
	download_links.append(srcs)
	

print(download_links)