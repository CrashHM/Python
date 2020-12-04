# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 11:20:02 2020

@author: hanno
"""

import json
import http.client
#assigns connection to 'conn'
conn = http.client.HTTPSConnection("bloomberg-market-and-financial-news.p.rapidapi.com")

#defines 'headers' as dictionary of user key and API host
headers = {
    'x-rapidapi-key': "55f56d852emsh5a169799e78b22bp132179jsn755647b81cb1",
    'x-rapidapi-host': "bloomberg-market-and-financial-news.p.rapidapi.com"
    }

#sends requst to API
conn.request("GET", "/market/get-price-chart?id=inmex%3Aind&interval=y1", headers=headers)

#presumably response is cached as conn.getresponse()
#HTTP repsonse (not human intelligable) set to 'res'
res = conn.getresponse()
print('res type: ',type(res))
#convert HTTP response to bytes set to 'data'
data = res.read()
print("data type: ", type(data))
#decodes bytes as utf-8 to create string set to text
text = data.decode('utf-8')
#print(text)
print('text type: ',type(text))
#takes json string and converts to dictionary
dict = json.loads(text)

#prints dictionary details
print('level 1 keys: ',dict.keys())
print('level 2 keys: ',dict['result'].keys())
print('level 3 keys: ',dict['result']['inmex:ind'].keys())
print('level 4 \'ticks\' is list and cannot have keys: list is indexed')
#print('level 5 keys: ',dict['result']['inmex:ind']['ticks'][0].keys())

#for line in dict['result']['inmex:ind']['ticks']:
 #  print(line)

'''

dict2 = dict['result']
print(dict2.keys())
dict3 = dict2['inmex:ind']
print(dict3.keys())
print(dict3.get('hasVolume'))
#print(dict3.get('ticks'))
#for line in dict3['ticks']:
#   print(line)
print(dict['result']['inmex:ind']['ticks'][0]['time'])
'''