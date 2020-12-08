#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 09:41:21 2020

@author: beowulf
"""

import numpy
import tabulate
import os
from numpy import genfromtxt


def importArray():
    cwd = os.getcwd()
    csv = cwd + '/AS6tshirt.csv'
    shirt_array = genfromtxt(csv, delimiter=',', encoding="utf-8")
    #shirt_array = genfromtxt('/home/beowulf/Documents/AS6tshirt.csv', delimiter=',', encoding="utf-8")
    return shirt_array

def arrayStats(array):
    
    results = numpy.array([numpy.nanmean(array),
               numpy.nanmedian(array),
               numpy.nanstd(array),
               numpy.nanmin(array),
               numpy.nanmax(array),
               numpy.nanpercentile(array,75)])
    results = numpy.round(results, decimals =2)
    return results

def array2list(array):
    list = array.tolist()
    return list

def displayTable(name,t,p):
    print(tabulate.tabulate([
        [name[0],t[0],p[0]],
        [name[1],t[1],p[1]],
        [name[2],t[2],p[2]],
        [name[3],t[3],p[3]],
        [name[4],t[4],p[4]],
        [name[5],t[5],p[5]]],
        headers = ['Values','Tshirt','Tshirt with Pocket']
        ))
def main():
    #mportData()
    array = importArray()
    resultnames = ['Mean',
                   'Meadian',
                   'Standard Deviation',
                   'Minimun Value',
                   'Maximum Value',
                   '75th Percentile']
    tShirt = arrayStats(array[:,1])
    pShirt = arrayStats(array[:,2])
    tShirtList = array2list(tShirt)
    pShirtList = array2list(pShirt)
    displayTable(resultnames,tShirtList,pShirtList)
main()