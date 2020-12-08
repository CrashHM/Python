#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 11:59:11 2020

@author: beowulf
"""
import http.client
import json

conn = http.client.HTTPSConnection("bloomberg-market-and-financial-news.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "55f56d852emsh5a169799e78b22bp132179jsn755647b81cb1",
    'x-rapidapi-host': "bloomberg-market-and-financial-news.p.rapidapi.com"
    }

conn.request("GET", "/market/get-price-chart?id=ibm%3Aus&interval=m3", headers=headers)

res = conn.getresponse()
data = res.read()
datadict = json.loads(data)
print(data)
for line in data:
    print (line)