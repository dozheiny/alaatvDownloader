#!/usr/bin/python

import io
import json
from bs4 import BeautifulSoup as bs, FeatureNotFound
import requests
import os

from src import quality
from src.quality import check_quality


def generate_link(url, just_link):
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

    total_videos_count = sum([len(i) for i in download_links])

    if not download_links or not total_videos_count:
        print("can't find video")
        exit()


    if just_link == True:
        with io.open('atd_output.txt', "a", encoding="utf-8") as file:
            for link_i, link_videos in enumerate(download_links):
                for videoI, videoLink in enumerate(link_videos):
                    file_a = videoLink + "\n"
                    file.write(file_a)


    else:
        with io.open('atd_output.sh', "a", encoding="utf-8") as file:
            file.write(f"#!/bin/bash\n")

            for course_i, course_videos in enumerate(download_links):
                for videoI, videoLink in enumerate(course_videos):
                    name = videoLink.split('/')[-1]
                    file.write(
                        'aria2c -x16 -s16 -k1M {} -o \"{:03d}_{}.mp4\"\n'.format(videoLink, videoI, name))

                    print(
                        f'Got {videoI + 1} videos out of {len(course_videos)} videos', end='\r')

        print(
            f'Got totally {total_videos_count} video form {len(download_links)} course')

        os.popen('sh atd_output.sh')
