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
    with open('/home/beowulf/Downloads/Street_Tree_List.csv','r') as datafile:
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
    print("Loading the database with %d items." % len(plist))

    # Open a connection the database
    con = sqlite3.connect(DBFILE)
    cur = con.cursor()

    #
    # Create the table if it's not there already
    #
    # The table has 3 columns, each with a data type associated:
    # - productID - unique product identifier, which is a TEXT type (string)
    # - description - a human-readable description, which is a TEXT type (string)
    # - quantity - amount of inventory, which a whole number (integer)
    #
    # Here, the table is dropped (deleted) first just to show an example.
    #
    #cur.execute("DROP TABLE %s" % DBTABLE)
    cur.execute("CREATE TABLE IF NOT EXISTS %s (TreeID TEXT PRIMARY KEY,qLegalStatus TEXT,qSpecies TEXT ,qAddress TEXT)" % DBTABLE)
    print(DBTABLE)

    # Adding the data can be done multiple ways:
    # 1) Row-by-row, looping through the list
    # 2) All at once using executemany(), which is best for inserting many rows at a time.
    # This example uses #2, requiring that we pass a list-of-lists to executemany()
    # where each list is of the format [ productID, description, quantity ] for an item.
    for i in range(len(plist)):
        cur.execute("INSERT INTO %s (TreeID, qLegalStatus, qSpecies, qAddress) VALUES (?,?,?,?)" % DBTABLE, plist[i])

    # This causes the above change to be flushed to the file.
    con.commit()

    # We are done with the database for now.
    con.close()
    
def deleteEnt():
    con = sqlite3.connect(DBFILE)
    cur = con.cursor()
    cur.execute("DROP TABLE %s" % DBTABLE)
    con.commit()
    con.close()
    
def query_Address():
    con = sqlite3.connect(DBFILE)
    cur = con.cursor()
    search = input('please enter string to search for: ')
    #
    # Make a LIKE query for a description.  We use a SELECT command for this and
    # specify the field of interest.   For full syntax:  https://sqlite.org/lang_select.html
    # Placing the '%' character at both ends of the search string means that the match
    # will occur if the string appears anywhere within the description column.
    #
    # To insert fields into the SQL command, use list with '?' in the string.  For example:
    # if you pass ?, ? in the string and do this: cur.execute("...", arg) it will be
    # substituted with arg1[0] and arg[1].
    #
   

    # Here is an example of an exact match
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
    #
    # Make a LIKE query for a description.  We use a SELECT command for this and
    # specify the field of interest.   For full syntax:  https://sqlite.org/lang_select.html
    # Placing the '%' character at both ends of the search string means that the match
    # will occur if the string appears anywhere within the description column.
    #
    # To insert fields into the SQL command, use list with '?' in the string.  For example:
    # if you pass ?, ? in the string and do this: cur.execute("...", arg) it will be
    # substituted with arg1[0] and arg[1].
    #
   

    # Here is an example of an exact match
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

         
def main():
    global CHOICE
    while CHOICE == '1' or CHOICE == '2' or CHOICE == '3' or CHOICE == '4' or CHOICE == '5':
        menuIn()
        if CHOICE =='1':
            print("Loading the database...")
            plist = array()
            print(plist[0])
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


   
