import os

uniArray = []  #global list to compensate for recursion
verbose = False #program state
hidfiles = 0 #global variable to compensate counting in recursion
numfiles = 0 #global variable to compensate counting in recursion

def getPath(): #gets user input for start directory. If no input uses current working directory.
    docs = '/home/beowulf/Documents'
    #docs = os.getcwd()
    path=input("please specify file path or press enter to use current working directory: ") #checks for input
    if path == '':
        path = docs
    if os.path.exists(path):
        return path
    else:
        return getPath()

def getSize(): #gets minimum file size from user. outputs float
    tempsize = input("Enter the minimum file size (MB) for search ")
    
    try:
        tempsize = float(tempsize)
    except:
        print("This will end badly, and it's all your fault :P")
    return tempsize
       
   #if tempsize.isnumeric():
   #  size = float(tempsize)
   #   return size
   #else:
   #    return getSize()


def isVerbose(): #gets input for verbose print of all paths explored
    global verbose
    temp = input("Verbose output?(y/n) ")
    if temp == 'y' or temp == 'Y':
        verbose = True
    elif temp == 'n' or temp == 'N':
        verbose = False
    else:
        return isVerbose()

        
def processDir(path):#creates 2d list from directry banch exploration. 
#Prints paths if program run as verbose.
    dirlist = os.listdir(path)
    global uniArray
    global verbose
    global numfiles,hidfiles
    for name in dirlist:
        fileP=path +'/'+name
        if os.path.isfile(fileP): #checks if file
            numfiles = numfiles + 1
            fileS = os.path.getsize(fileP)/1048576 #converts size to MB
            if verbose:
                print(fileP)
            newrow = [name,fileS,fileP]
            uniArray.append(newrow)
        elif os.path.isdir(fileP): #check if directory. if directory runs 
#processDir(). prints directory
            #rowcnt =+ rowcnt
            numfiles = numfiles + 1
            fileS = os.path.getsize(fileP)
            if verbose:
                print(fileP)
            processDir(fileP)
        else:# counts hidden files and directories 
            hidfiles = hidfiles +1
        
def directSelect(size):#iterates throuh uniArray anc compares values to 
#input size. Prints result.
    global uniArray
    neatTable = []
    rows = len(uniArray)
    print('The following files are greater than ',size,' MB')
    print('File Name \t\t Size \t\t File Path')
    for cnt in range(rows):
        fileS = float(uniArray[cnt][1])
        if fileS >= size:
            strsize = '%.2f MB' %uniArray[cnt][1]
            print(uniArray[cnt][0],'\t',strsize,'\t',uniArray[cnt][2])
    
            
def main():
    path = getPath()
    size =getSize()
    isVerbose()
    processDir(path)
    print()
    print(numfiles,' files and directories were searched.')
    print(hidfiles,' hidden files and directories were ignored.')
    print()
    directSelect(size)
    #print(uniArray)
    #print(tempfile.read())
    #tempfile.close()
    
main()

