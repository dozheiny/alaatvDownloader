from bs4 import BeautifulSoup as bs
import requests
    
url = 'https://alaatv.com/set/963'
req = requests.get(url).text

soup = bs(req, 'lxml')
tags = soup.find_all('script')
s = soup.find('script', type='application/ld+json')


for link in soup.find_all('script', type='application/ld+json'):

	if 'https://' in str(link):
		print(link)

