#!/usr/bin/env python3

#
# This file shows how to create a SQLite table in a file, store data in it,
# and run a query.
#
# The filename and table are set in the variables DBFILE and DBTABLE.
# An SQLite file can contain multiple tables.
#
# The table holds a series of (fake) retail products
# uniquely identified by a stock code.
#


import sqlite3
CHOICE = '1'
DBFILE = 'inventory.db'
DBTABLE = 'Trees'

# The list of products
def array():#creates 2d list from csv. removes non primary key lines. First column assumed to be primary key.
    treelist = []
    #1filename = input('Please input the path for the desired file: ')
    filename = '/home/beowulf/Downloads/Street_Tree_List.csv'
    with open(filename,'r') as datafile:
        for line in datafile:
            linelisttemp = line.split(',')
            linelist = linelisttemp[:4]
            for i in range(4):
                if i == '':
                    linelist[i] = 0
            if linelist[0].isdigit() and len(linelist) == 4:#Limits inclusion to rows with key value
                treelist.append(linelist)
    datafile.close()
    
    return treelist

def load_db(plist):
    global TABLELOAD
    print("Loading the database with %d items." % len(plist))
    
    
    deleteEnt()
        #cur.execute("DROP TABLE %s" % DBTABLE)
    con = sqlite3.connect(DBFILE)
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS %s (TreeID TEXT PRIMARY KEY,qLegalStatus TEXT,qSpecies TEXT ,qAddress TEXT)" % DBTABLE)
    for i in range(len(plist)):
        cur.execute("INSERT INTO %s (TreeID, qLegalStatus, qSpecies, qAddress) VALUES (?,?,?,?)" % DBTABLE, plist[i])
    con.commit()
    con.close()
    
def deleteEnt():
    global TABLELOAD
    #if TABLELOAD == 0:
    #    print('ssdddddddddd')
    #    return
    con = sqlite3.connect(DBFILE)
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS %s" % DBTABLE)
    con.commit()
    con.close()
    
    
def query_Address():
    con = sqlite3.connect(DBFILE)
    cur = con.cursor()
    search = input('please enter string to search for: ')
    search = '%'+search+'%'
    qkey = (search,)
    recs = cur.execute("SELECT * FROM %s WHERE qAddress LIKE ?" % DBTABLE, qkey)
    print('Records that match:')
    for r in recs:
       print("TreeID: %s" % r[0])
       print("qLegalStatus: %s" % r[1])
       print("qSepcies: %s" % r[2])
       print("qAddress: %s" % r[3])
       print()
    con.close()
    
def query_Species():
    con = sqlite3.connect(DBFILE)
    cur = con.cursor()
    search = input('please enter string to search for: ')
    search = '%'+search+'%'
    qkey = (search,)
    recs = cur.execute("SELECT * FROM %s WHERE qSpecies LIKE ?" % DBTABLE, qkey)
    print('Records that match:')
    for r in recs:
       print("TreeID: %s" % r[0])
       print("qLegalStatus: %s" % r[1])
       print("qSepcies: %s" % r[2])
       print("qAddress: %s" % r[3])
       print()
    con.close()
        
def menuIn():
    global CHOICE
    print('San Franciso Trees Database\nMenu Options:\n'
          '1) Bulk read enteries from file\n'
          '2) Delete all enteries\n'
          '3) Query by species\n'
          '4) Query by address\n'
          '5) Exit')
    CHOICE = input('Enter your choice: ')
    if CHOICE == '1' or CHOICE == '2' or CHOICE == '3' or CHOICE == '4' or CHOICE == '5':
        return
    else:
        menuIn()
         
def main():
    global CHOICE
    while CHOICE == '1' or CHOICE == '2' or CHOICE == '3' or CHOICE == '4' or CHOICE == '5':
        menuIn()
        if CHOICE =='1':
            print("Loading the database...")
            plist = array()
            load_db(plist);
            print("Done.")
            print()
        if CHOICE == '2':
            deleteEnt()
            print('All enteries deleted')
            print()
        if CHOICE == '4':
            query_Address()
            print()
        if CHOICE =='3':
            query_Species()
            print()
        if CHOICE == '5':
            CHOICE = '6'
            print('Good Bye!')
    if not CHOICE == '6':
        print('You have cause the program to cease functioning.')
main()


   
