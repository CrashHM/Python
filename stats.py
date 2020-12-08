# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 09:59:34 2020

@author: murph9h
"""
import pandas as pd
import math

def array():
    treelist = []
    with open('E:\\ArcGIS_Projects\\SewerStructuresUpdate\\StructRimWcontours.csv','r') as datafile:
        for line in datafile:
            line = line.rstrip()
            linelist = line.split(',')
            #if linelist[0].isdigit():
            
            treelist.append(linelist)
            #else:
            #    pass
        treelist.remove(treelist[0])
        for i in range(10):
            print(treelist[i])
            
def dFrame():
    '''Reads in Data from Csv'''
    df=pd.read_csv('E:\\ArcGIS_Projects\\SewerStructuresUpdate\\WorkingTable.csv')
    #df=df.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)
    print(df.head(5))

    #for col in df.columns: 
    #    print(col)
    return df
'''
Attempt to create empty column. 
def newCOL(df,name):
    mtList = [float()]
    dfLen = len(df.index)
    for i in range(dfLen):
        mtList.append()
    df[name]=mtList
    return df

'''
def newcol(df,name):
    '''Creates new column, sets data type to  numberic'''
    df.insert(4,name,int)
    df[name]=pd.to_numeric(df[name], errors='coerce')
    return df
    
def calcDiff(df):
    cnt = 0
    for row in range(len(df.index)):
        rimTemp = df.iloc[row,1]
        conTemp = df.iloc[row,3]
        if rimTemp == 0 or conTemp == None or conTemp == None or conTemp == 0:
            cnt = cnt + 1
            #print(row,' ',rimTemp,' ',conTemp)
            #df.iat[row,1] = nan
            #df.iat[row,3] =  nan
            df2=df.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)
    #print(len(df.index),' 'len(df2.index))
    for row in range(len(df2.index)):
        rimTemp = df.iloc[row,1]
        conTemp = df.iloc[row,3]
        rimDiffTemp = rimTemp - conTemp
        df2.iat[row,4] = rimDiffTemp
        #df.iat[row,5] = math.sqrt(rimDiffTemp**2)
    #df=df.drop([droplist],axis=0)
    print('Rows Dropped for 0 or NULL: ',cnt)
    print(df2.head(100))
    return df2


        
def stats(df,col):
    diffTemp = df.iloc[:,col]
    #print(diffTemp.describe())
    print()  
    print('Median: ',diffTemp.median())
    print('Mode: ',diffTemp.mode())
    print('Mean: ',diffTemp.mean())
    print('Standard Deviation: ',diffTemp.std())
    print('Maximum: ',diffTemp.max())
    print('Minimum: ',diffTemp.min())
    print()
    print()
   
    
def main():
    #array()
    name = 'rimdiff'
    df = dFrame()
    #df = newCOL(df,name)
    df = newcol(df, name)
    #df = newCOL(df, 'ABS Diff')
    df = calcDiff(df)
    #df = absDiff(df)
    print('Rim Elevation Stats')
    stats(df,1)
    print('Nearest Contour Stats')
    stats(df,3)
    print('Difference of Rim and Near Contour Stats')
    stats(df,4)
    df.to_csv(r'E:\\ArcGIS_Projects\\SewerStructuresUpdate\\ProcessedTable.csv', index = False)
main()
