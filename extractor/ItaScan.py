#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright (c) 2019 BugNoFix. Under MIT License.

import requests, re, os, json
from re import sub

# Load configs
#CONFIG = json.load(open('setting.json'))

ItaScan_Valid="https:\/\/itascan\.info\/.*"

def Itascan():
    url = input("Inserisci l'intera pagina: ")
    page = requests.get(url).text
    print("Pag caricata")
    url = []
    nome = []
    n = 0
    #creo un array con tutti i capiti e ogni spazio contiene una tupla
    dati = re.findall(r'<td> <a rel="nofollow" href="(.*?)">(.*?)<\/a> <\/td>', str(page))
    for metadati in dati:
        url.append(metadati[0])
        nome.append(metadati[1])

    print(nome)

    
Itascan()