#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 15:27:34 2020

@author: beowulf
"""

import django.core.validators
import pandas as pd
import urllib.request



def insertColumn(df,colNum,name):
    
    '''Creates new column, sets data type to  numberic'''
    df.insert(colNum,name,int)
    #df[name]=pd.to_numeric(df[name], errors='coerce') #converts column to numeric
    return df

def webValid(link):#checks for valid web address. Does not validate
    validate = django.core.validators.URLValidator()
    print(validate(link))
    '''
    try:
        validate(link)

    except ValidationError as exception:'''
        


def url_is_alive(url):
    """
    Checks that a given URL is reachable.
    :param url: A URL
    :rtype: bool
    """
    request = urllib.request.Request(url)
    request.get_method = lambda: 'HEAD'

    try:
        urllib.request.urlopen(request)
        return True
    except urllib.request.HTTPError:
        return False

def looper(df):#Checks weblinks for Monument sheets  and Sewer sheets based on CSV. 
#In this case the csv provides the file number and the link pattern is known.
    for i in range(len(df.index)):
        monumentFile = str(df.iat[i,2])
        monumentWeb = 'http://oakbec.s3.amazonaws.com/Archive/MonumentSheets/'
        sewerWeb = 'https://oakbec.s3.amazonaws.com/Archive/SewerSheets2ndFloor/SS' 
        sewerFile = str(df.iat[i,1]) 
        pdf = '.pdf'
        monumentComplete = monumentWeb + monumentFile + pdf
        sewerComplete = sewerWeb + sewerFile + pdf
        df.iat[i,4] = url_is_alive(sewerComplete)
        df.iat[i,5] = url_is_alive(monumentComplete)
    return df

def looper2(df):#checks weblinks from list of links in csv. Checks length of string 
#as proxy for valid url formatting.
    for i in range(len(df.index)):
        
        link1 =df.iat[i,4]
        link2 = df.iat[i,3]
        link3 = df.iat[i,2]
        link4 = df.iat[i,1]
        linkList = [link1,link2,link3,link4]
        cnt = 12
        for link in linkList:
            if len(str(link)) < 20:
                df.iat[i,cnt]= 'NoLink'
            else:
                linkBool = url_is_alive(link)
                df.iat[i,cnt] = linkBool
                if not linkBool:
                    print(df.iloc[i,5])
                
            cnt = cnt + 1
           
    return df

def main():
    df = importData()
    df = insertColumn(df,12,'Link1True')
    df = insertColumn(df, 13, 'Link2True')
    df = insertColumn(df, 14, 'Link3True')  
    df = insertColumn(df, 15, 'Link4True')
    df = looper2(df)
    print(df[df.columns[12:16]].head(5))
    df.to_csv('/home/beowulf/Downloads/As_BuiltTablePy.csv')
    #print(url_is_alive('https://oakbec.s3.amazonaws.com/Archive/SewerSheets2ndFloor/SS155.pdf'))

main()