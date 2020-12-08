
# This program opens a window and displays information based on a Button event.

import tkinter

class ShowInfoGUI:
    def __init__(self):
        # Create the main window
        self.main_window = tkinter.Tk()

        # Create two frames
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)
        
        # Create a blank label in the top frame
        self.value = tkinter.StringVar()
        self.address_label = tkinter.Label(self.top_frame, \
                    textvariable= self.value)
                       
        # Create the two buttons in the bottom frame
        self.address_button = tkinter.Button(self.bottom_frame, \
                text = 'Show Info', command = self.show_info)
        self.quit_button = tkinter.Button(self.bottom_frame, \
                text = 'Quit', command = self.main_window.destroy)

        # Pack the label
        self.address_label.pack()
        #Pack the buttons
        self.address_button.pack(side = 'left')
        self.quit_button.pack(side = 'left')

        # Pack the frames
        self.top_frame.pack()
        self.bottom_frame.pack()

        # Enter the tkinter main loop
        tkinter.mainloop()

    # Define the show_info function
    def show_info(self):
        self.value.set('Steven Marcus\n274 Baily Drive\n' \
                       'Waynesville, NC 27999')

# Create an instance of ShowInfoGUI
show_info = ShowInfoGUI()    





import sqlite3
CHOICE = '1'
DBFILE = 'inventory.db'
DBTABLE = 'Trees'

# The list of products
def array():#creates 2d list from csv. removes non primary key lines. First column assumed to be primary key.
    treelist = []
    #filename = input('Please input the path for the desired file: ')
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
    
'''   
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
'''   
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
'''        
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
'''         
def main():
   
            print("Loading the database...")
            plist = array()
            load_db(plist)
            query_Species()
            print()
       
main()


   
