#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright (c) 2018 BugNoFix. Under MIT License.
import requests, re, os, json

CONFIG = json.load(open('setting.json'))

def MangaRock(url):
    page = requests.get(url).text
    all_image = re.findall(r'<a href="\/manga\/mrs-serie-.*?\/chapter\/mrs-chapter-(.*?)"', page)
    dirName = 'prova'
    a = 0
    while True:
        
        #page = requests.get(url + '/' + 'chapter/mrs-chapter-' + all_image[0])
        #print(all_image[0])
        #image = re.findall(r'data:image.*', str(page))
        #search_image = re.search(r'(data:image\/webp;base64,.*)', str(image))
        filename = str(a) + '.jpg'
        print("Download: " + filename)
        #print(image)
        r = requests.get('https://mangarock.com/manga/mrs-serie-241688/chapter/mrs-chapter-100321292')
        open(CONFIG['Path'] + dirName + '/' + filename, 'wb').write(r.content)
        #del(all_image[0])
        a = a + 1

url = input('Inserisci il link del manga: ')
MangaRock(url)
