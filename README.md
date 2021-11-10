# alaaTV downloader 🤩

## Table of contents
* [General info](#general-info)
* [Update](#update)
* [Requirements](#requirements)
* [setup](#setup)
* [usage](#usage)

## general-info 🐱‍🚀
alaatv does not allow you to download the playlist you want, you should to open the tab all the time and download your video, this is so hard that's why Erfan and i came and wrote this webscrap for you guys .

## update ! (ver 0.2)

now you can have just download links to import your favorite Downloader

you can use that with ```-link=True``` argument .
## Requirements 👾
install packages from source :

[python](https://python.org)
[aria2](http://aria2.github.io/)


if you are on LINUX or MAC OS :
```
sudo [dnf / yum / apt-get] install python3 aria2 python3-pip git
```
and if you are windows user install files from link that i said

## Setup 👀
first of all , check requirements installed 
```
python3 --version
```
```
aria2c -v
```
```
pip -v
```
```
git --version
```

if you get version output , that seems everything working fine !
after that , install requirements

1️⃣ clone the project:
```
git clone https://github.com/dozheiny/alaatvDownloader.git
```
2️⃣ change directory to project
```
cd alaatvDownloader
```
3️⃣ install the library you need
```
pip install -r requirements.txt
```

## Usage 🐱‍👤
normal usage :
```
python3 alaatvDownloader.py [link] -q [240, 480, 720] -l [True/False]
```

Arguments :
```
positional arguments:
  url                   enter url of your playlist to download your videos

optional arguments:
  -h, --help            show this help message and exit
  -q QUALITY, --quality QUALITY
                        enter quality you want to download
  -l LINK, --link LINK  just get download link(without download)

```

Example :
```
python3 alaatvDownloader.py "https://alaatv.com/set/963"
python3 alaatvDownloader.py "https://alaatv.com/set/963" -q 480 --link True
python3 alaatvDownloader.py "https://alaatv.com/set/963" --link True
```
the default quality is 480

the default link finder is off, you can use that with ```-l True```

hope enjoy well 🧙‍
