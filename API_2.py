# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 08:35:03 2020

@author: hanno
"""

URL = 'https://opendata.arcgis.com/datasets/28e2bdcee7cc471e9e0ca943ca7acef3_0.geojson'

import json
import urllib

# streamlined workflow to access json
data = urllib.request.urlopen(URL).read().decode()   

# json -> dict?
dict = json.loads(data)
'''
#testing list result for .keys() trying to figure out odd notebook issue
#notebooks seems to create list form json.loads()
print(type(dict))
print(dict.keys())

sTring = [1,2,3]
print(type(sTring))
print(sTring.keys())
'''

'''
data = urllib.request.urlopen(url).read().decode()
#streamlined work flow
'''