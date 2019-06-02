#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright (c) 2018 BugNoFix. Under MIT License.

from extractor import *
import requests, re, os, json

# Load configs
CONFIG = json.load(open('setting.json'))

def MangaDownloader(url):
    if re.compile(ShonenJumpPlus_Valid).match(url):
        ShonenJumpPlus(url)

url = input('Inserisci il link del manga: ')
MangaDownloader(url)


 
