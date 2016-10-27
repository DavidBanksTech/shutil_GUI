from tkinter import *
from tkinter import filedialog
import os
import time
import datetime
import shutil

def start_folder():
    dir1 = filedialog.askdirectory()
    var_src.set(dir1)
    """if dir1:
        print (dir1)"""

def destination_folder():
    dir2 = filedialog.askdirectory()
    var_dest.set(dir2)
    """if dir2:
        print (dir2)"""


def modmove(source,dest1):
    source = var_src.get()
    #print("source: {}".format(source))
    dest1 = var_dest.get()

    for _files in os.listdir(source):  
        if _files.endswith(".txt"):
            #print("_files: {}".format(_files))
            src_path = os.path.join(source,_files)
            #print("src_path: {}".format(src_path))
            dest_path = os.path.join(dest1,_files)
                
            mtime = (os.path.getmtime(src_path))
            timeDiff = time.time() - mtime #Difference from time of file creation or modification until current time
            _24hrsAgo = time.time() - (24 *60 *60) #Epoc time for a 24hr period is 86400 seconds
            last24hrs = time.time() - _24hrsAgo #Seconds that have occured within the last 24 hr period
            
            if mtime > _24hrsAgo:
                shutil.copy(src_path,dest_path)
                print ("src_path: {},\n Copied to: {}".format(src_path,dest_path))


        


root = Tk()
f = Frame(root)

sourcebutton =      Button(f, text = "Choose Folder", command = start_folder)
destinationbutton = Button(f, text = "Destination"  , command = destination_folder)
runbutton =         Button(f, text = "Run", command = lambda: modmove(start_folder,destination_folder))

var_src = StringVar()
var_dest = StringVar()

txt_src = Entry(f, textvariable=var_src)
txt_dest = Entry(f, textvariable=var_dest)

sourcebutton.pack(side = LEFT)
txt_src.pack(side = LEFT)
destinationbutton.pack(side = LEFT)
txt_dest.pack(side = LEFT)
runbutton.pack(side = LEFT)


l = Label(root, text = 'uMod')
l.pack()
f.pack()

