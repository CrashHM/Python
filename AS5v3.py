# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 07:41:29 2020

@author: hanno
"""
import urllib
import json
import sys
class Daylite:
    def __init__(self,lat,long,date ='today'):
        self.URL = 'https://api.sunrise-sunset.org/json?lat='+str(lat)+'&lng='+str(long)+'&date='+str(date) 
        inputFile = urllib.request.urlopen(self.URL)    
        self.s = inputFile.read()    
        self.dict = json.loads(self.s)
        print('Testing latitude = ',lat,', longitude = ',long,', date = ',date)
        if self.dict['status'] == 'OK':
            pass
        else:
            print('Information unavailible at this time.')
            sys.exit()

    def get_sunrise(self):
        print('Sunrise: ',self.dict['results']['sunrise'])
    
    def get_sunset(self):
        print('Sunset: ',self.dict['results']['sunset'])

    def get_daylength(self):
        print('Day Length: ',self.dict['results']['day_length'])




def main():
    
    
    day1=Daylite(37.952,-122.073)
    day1.get_sunrise()
    day1.get_sunset()
    day1.get_daylength()

    print()
   
    day3=Daylite(37.952,-122.073,'2020-10-11')
    day3.get_sunrise()
    day3.get_sunset()
    day3.get_daylength()
    
main()