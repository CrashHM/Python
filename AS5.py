# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 07:41:29 2020

@author: hanno
"""
import urllib
import json
import sys
URL = "https://api.sunrise-sunset.org/json?lat=36.7201600&lng=-4.4203400"
def getParam():
    lat = input('Latitude: ')
    long = input('Long: ')
    date = input('Date as YYYY-MM-DD or \'T\' for today: ')
    if date == 't' or date =='T':
        date = 'today'
    return lat,long,date

def urlMake(lat,long,date):
    global URL
    URL = 'https://api.sunrise-sunset.org/json?lat='+lat+'&lng='+long+'&date='+date
    
def apiCall():    
    inputFile = urllib.request.urlopen(URL)    
    s = inputFile.read()    
    dict = json.loads(s)
    if dict['status'] == 'OK':
        return dict
    else:
        print('Information unavailible at this time.')
        sys.exit()

def sunrise(dict):
    print('Sunrise: ',dict['results']['sunrise'])
    
def sunset(dict):
    print('SunsetL ',dict['results']['sunset'])

def daylength(dict):
    print('Day Length: ',dict['results']['day_length'])
    
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