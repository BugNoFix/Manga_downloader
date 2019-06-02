#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright (c) 2018 BugNoFix. Under MIT License.

import requests, re, os, json
from PIL import Image

# Load configs
CONFIG = json.load(open('setting.json'))

ShonenJumpPlus_Valid="https:\/\/shonenjumpplus.com.*"

def decompiler(nome):
    image = nome
    original = Image.open(image)
    #Questo sarà il file che conterra 
    im = Image.new("RGB", (822,1200), "white")

    x = [0, 200, 0, 400, 200, 400, 600, 0, 600, 200, 600, 400]
    y = [296, 0, 592, 0, 592, 296, 0, 888, 296, 888, 592, 888]
    w = 200
    h = 296
    #xP = [200, 0, 400, 0, 400, 200, 0, 600, 200, 600, 400, 600]
    #yP = [0, 296, 0, 592, 296, 592, 888, 0, 888, 296, 888, 592]
    for z in range(1,7):

        #taglio le 2 immagini complementari
        imagePart1 = original.crop((x[0], y[0], w + x[0], h+ y[0])) 
        imagePart2 = original.crop((x[1], y[1], w + x[1], h+ y[1])) 
        #incollo le 2 immagini complementari
        original.paste(imagePart1, (x[1],y[1]))#inverto le 2 cordinate di x e y perche son complementari
        original.paste(imagePart2,(x[0],y[0]))  
        del(x[0], y[0])
        del(x[0], y[0])
    original.save(nome)

def ShonenJumpPlus(url):
    page = requests.get(url).text
    number_page = re.search('<span class="viewer-slider-pagenum-last rtl js-viewer-slider-pagenum-last">(.*)<\/span>', page).group(1)
    all_image = re.findall(r'data-src="https:\/\/cdn-ak-img\.shonenjumpplus\.com\/public\/page\/......................................................."', page)
    dirName = re.search('<h1 class="episode-header-title">(.*)<\/h1>', page).group(1)
    try:
        # Create target Directory
        os.mkdir(CONFIG['Path'] + dirName)
        print('Directory ' + CONFIG['Path'] + dirName + ' creata') 
    except FileExistsError:
        print(' I file all\' interno della directory ' + CONFIG['Path'] + dirName + ' verranno sovrascritti')
    base_url = 'https://cdn-ak-img.shonenjumpplus.com/public/page/'
    a = 0
    try:
        while a != number_page:
            image = re.search(r'data-src="https:\/\/cdn-ak-img\.shonenjumpplus\.com\/public\/page\/(.......................................................)"', str(all_image))
            url = base_url + image.group(1)
            filename = str(a) + '.jpg'
            print("Download: " + filename)
            #download the image
            r = requests.get(url, allow_redirects=True)
            dire = CONFIG['Path'] + dirName + '/' + filename
            open(dire , 'wb').write(r.content)
            #remove from list the first link
            del(all_image[0])
            decompiler(dire)
            print("Decompile image: " + str(a))
            a = 1 + a
    except AttributeError:
        print("Tutte le immagini sono state scaricate")


 
