#!/usr/bin/python
import argparse
from src import alaatv


def usage():
    return '''
    Usage:
        python3 main.py [link] -q [240, 480, 720]

    example:
        python3 main.py "https://alaatv.com/set/963"
        python3 main.py "https://alaatv.com/set/963" -q 480
    The default quality is 480.
    '''


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="alaatv.com playlist downloader", usage=usage())
    parser.add_argument('url', type=str, help='enter url of your playlist to download your videos')
    parser.add_argument('-q', '--quality', type=int, help='enter quality you want to download', default=480)

    args = parser.parse_args()
    url = args.url
    quality = args.quality

    if args.quality:
        alaatv.main(url)
    else:
        usage()


