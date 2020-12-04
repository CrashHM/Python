# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 09:44:40 2020

@author: hanno
"""

import urllib
import json

URL = 'https://opendata.arcgis.com/datasets/cad5f745a6ca4d0aa2601fd2c29ced1a_0.geojson'
def apiCall():    
    inputFile = urllib.request.urlopen(URL)    
    s = inputFile.read()  
    #dict = json.loads(s)
    #return dict

def pretty(d, indent=0):
   for key, value in d.items():
      print('\t' * indent + str(key))
      if isinstance(value, dict):
         pretty(value, indent+1)
      else:
         print('\t' * (indent+1) + str(value))
'''
def main():
    dict = apiCall()
    dkey =dict.keys()
    print(dict['features'][1].keys())
    print('crs: ',dict['crs'])
    #for i in range(20):
    print(dict['features'][1])
    for key in dkey:
        print('\n',key,': \n')
        #print(dict[key])
'''
def main():
    apiCall()
    
    
main()