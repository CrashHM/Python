#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 17:11:54 2020

@author: beowulf
"""

''' this was an initial idea for reference by key values
def dict():#creates dictionary from csv. Removes non primary key lines. References by primary key.
    dict={}
    with open('/home/beowulf/Downloads/Street_Tree_List.csv','r') as datafile:
        for line in datafile:
            linelist = line.split(',')
            if linelist[0].isdigit():
                dict[linelist[0]] = linelist
            else:
                pass
    datafile.close()
    return dict
'''

def array():#creates 2d list from csv. removes non primary key lines. First column assumed to be primary key.
    treelist = []
    filename = input('Please input the path for the desired file: ')
    #filename = '/home/beowulf/Downloads/Street_Tree_List.csv'
    with open(filename,'r') as datafile:
        for line in datafile:
            linelist = line.split(',')
            if linelist[0].isdigit():#Limits inclusion to rows with key value
                treelist.append(linelist)
            else:
                pass
    datafile.close()
    return treelist
'''
def searchReg(treelist):
    pineCount = 0
    mPineCount = 0
    dpwMaint = 0
    for i in range(len(treelist)):
        if not re.search(r'Pine',treelist[i][2]) == None or not re.search(r'pine',treelist[i][2]) == None:
            pineCount = pineCount +1
            if not re.search(r'DPW', treelist[i][1]) == None:
                dpwMaint = dpwMaint +1
            if not re.search(r'Monterey',treelist[i][2]) == None:
                mPineCount = mPineCount +1
    print("There are ",pineCount," pine trees registered in San Francisco.")
    print('There are ',dpwMaint,' Pine trees maintained by the the City of San Francisco')
    print("There are ",mPineCount," Moneterey pines registered in San Francisco.")
'''    
    
def speclist(treelist):#create list of unique species entries from list
    species = [treelist[0][2]]
    for i in range(len(treelist)):
        tree = treelist[i][2]
        entertree = True
        for ii in species:
            if ii == tree:
                entertree = False
        if entertree:
            species.append(tree)
    species.sort()
    return species

def stumpgrinder(treelist):
    for tree in treelist:
        filterlist = tree.split('::')
        temptree = str(filterlist[0])
        temptree = temptree.rstrip()
        if len(temptree) < 5:
            pass
        elif temptree == 'Tree(s)' or temptree == 'Shrub':
            pass
        else:
            print(temptree)
        
#def specCounter(treelist,speclist):
    
#    for i in range(len(treelist)):
        


     
def main():
    treelist = array()
    treelist = speclist(treelist)
    stumpgrinder(treelist)
    
main()