# alaaTV downloader 🤩

## Table of contents
* [General info](#general-info)
* [Requirements](#requirements)
* [setup](#setup)
* [usage](#usage)

## general-info 🐱‍🚀
alaatv does not allow you to download the playlist you want, you should to open the tab all the time and download your video, this is so hard that's why Erfan and i came and wrote this webscrap for you guys .

## Requirements 👾
[python](https://python.org)
[aria2](http://aria2.github.io/)
if you are on LINUX or MACOS :
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
aftar that , install requirements

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
python3 setup.py
```

## Usage 🐱‍👤
normal usage :
```
python3 main.py [link] -q [240, 480, 720]
alaatv.com playlist downloader
```
Example :
```
python3 main.py main.py "https://alaatv.com/set/963" -q 480
```
the default quality is 480
hope enjoy well 🧙‍
