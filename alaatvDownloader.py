#!/usr/bin/python
import argparse
from src import alaatvLinkFinder


def usage():
    return '''
    Usage:
        python3 main.py [link] -q [240, 480, 720] [link or download]

    example:
        python3 main.py "https://alaatv.com/set/963"
        python3 main.py "https://alaatv.com/set/963" -q 480 --link True
        python3 main.py "https://alaatv.com/set/963" --link True

        
    The default quality is 480.
    The default link maker is False
    '''


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="alaatv.com playlist downloader", usage=usage())
    parser.add_argument('url', type=str, help='enter url of your playlist to download your videos')
    parser.add_argument('-q', '--quality', type=int, help='enter quality you want to download', default=480)
    parser.add_argument('-l','--link', type=bool, help="just get download link(without download)", default=False)


    args = parser.parse_args()
    url = args.url
    quality = args.quality
    just_link = args.link

    if args.quality:
        alaatvLinkFinder.generate_link(url, just_link)
    else:
        usage()

