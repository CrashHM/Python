# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 20:00:34 2020

@author: hanno
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 07:41:29 2020

@author: hanno
"""
import urllib
import json
import sys
class Daylite:
    def__init__(self,lat,long,date)
        self.lat = 
        self.long = 
        self.date =

'''
def getParam():
    lat = input('Latitude: ')
    long = input('Long: ')
    date = input('Date as YYYY-MM-DD or \'T\' for today: ')
    if date == 't' or date =='T':
        date = 'today'
    return lat,long,date
'''
def urlMake(self,lat,long,date='today'):
    self.URL = 'https://api.sunrise-sunset.org/json?lat='+lat+'&lng='+long+'&date='+date
    return self.URL
    
def apiCall(self,self.URL):    
    inputFile = urllib.request.urlopen(self.URL)    
    s = inputFile.read()    
    dict = json.loads(s)
    if dict['status'] == 'OK':
        return dict
    else:
        print('Information unavailible at this time.')
        sys.exit()

def sunrise(lat,long,date='today'):
    self.dict = apiCall(self.URL)
    print('Sunrise: ',self.dict['results']['sunrise'])
    
def sunset(lat,long,date='today'):
    self.URL = urlMake(lat, long, date)
    self.dict = self.apiCall(URL)
    print('SunsetL ',self.dict['results']['sunset'])

def daylength(lat,long,date='today'):
    self.URL = urlMake(lat, long, date)
    self.dict = apiCall(self.URL)
    print('Day Length: ',self.dict['results']['day_length'])
    
def main():
    lat,long,date = getParam()
    urlMake(lat,long,date)
    dict = apiCall()
    sunrise(dict)
    sunset(dict)
    daylength(dict)
def main2():
    lat,long,date = getParam()
    urlMake(lat,long,date)
    dict = apiCall()
    print(dict)
main()
#main2()