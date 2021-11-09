#!/usr/bin/python

import io
import json
from bs4 import BeautifulSoup as bs, FeatureNotFound
import requests
import argparse
import os

# TODO: make a seprate download list file (.sh) for each search
# TODO: don't write already exist download link to file
# TODO: find name of each download link

def usage():
    return '''
    Hello !
    main.py [link] -q [240, 480, 720]
    main.py "https://alaatv.com/set/963"
    main.py "https://alaatv.com/set/963" -q 480
    The default quality is 480.
    '''

def main(url):
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

        srcs = [link['src'] for link in source if 'src' in link.attrs and check_quality(quality) in str(link)]
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

    os.popen('sh atd_output.sh')   


def check_quality(quality):
    if quality == 240:
        return '/240p/'

    elif quality == 720:
        return '/HD_720p/'

    else:
        return '/hq/'          

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="alaatv.com playlist downloader", usage=usage())
    parser.add_argument('url', type=str, help='enter url of your playlist to download your videos')
    parser.add_argument('-q', '--quality',type=int, help='enter quality you want to download', default=480)

    args = parser.parse_args()
    url = args.url
    quality = args.quality

    if args.quality :
        main(url)
    else:
        usage()
