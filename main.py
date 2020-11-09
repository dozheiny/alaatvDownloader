# load libraries
import io
import json
import sys
from bs4 import BeautifulSoup as bs, FeatureNotFound
import requests

# TODO: make a seprate download list file (.sh) for each search
# TODO: don't write already exist download link to file
# TODO: find name of each download link

# NOTE: Too much for loop in code, may find better solutions

if len(sys.argv) > 1:
    url = sys.argv[1]
else:
    url = 'https://alaatv.com/set/963'

req = requests.get(url).content
course_links = []
download_links = []

try:
    soup = bs(req, 'lxml')
except FeatureNotFound:
    soup = bs(req, 'html.parser')

for link in soup.find_all('script', type='application/ld+json'):
    data_dict = json.loads(link.string)
    items = data_dict.get('itemListElement', [])
    for item in items:
        course_links.append(item.get('url', ''))


for course_link in course_links:

    request = requests.get(course_link).content
    soup_ = bs(request, 'html.parser')
    source = soup_.find_all('source')
    srcs = [link['src'] for link in source if 'src' in link.attrs]

    download_links.append(srcs)

total_vidoes_count = sum([len(i) for i in download_links])

if not download_links or not total_vidoes_count:
    print('No video found')
    exit()

with io.open('atd_output.sh', "a", encoding="utf-8") as file:
    file.write(f"#!/bin/bash\n")
    for course_i, course_videos in enumerate(download_links):
        for vidoe_i, videoLink in enumerate(course_videos):
            name = videoLink.split('/')[-1]
            file.write(
                'aria2c -x16 -s16 -k1M {} -o \"{:03d}_{}.mp4\"\n'.format(videoLink, vidoe_i, name))
            print(
                f'Got {vidoe_i+1} videos out of {len(course_videos)} vidoes', end='\r')

print(
    f'Got totaly {total_vidoes_count} video form {len(download_links)} course')

# print(download_links)
