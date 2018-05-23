#!/usr/bin/python

#################################################################################
# Tool Name       : LocateNewFiles.py                        
#
# Author          : Tarig Mudawi        
#                   Dakota State University
#
# Tool Description: This tool gets its input as a directory folder, a time interval 
#                   in minutes and a P/S flag to either Print to screen or Save to 
#                   a file a list of all files that are created or modified within 
#                   the timeframe that the use specified.          
#                    This help when the user suspects that some suspisios files 
#                    are created by some sort of a hacker attack. 
##################################################################################   

import os
import datetime as dt
import sys

def ListToFile(MyList):
    '''Populate the file from the passed list of suspected files''' 

    #Open the file for writing
    with open('C:\FilesToInspect\NewlyCreatedOrModifiedFiles.txt', 'w') as file_handler:
        for item in MyList:
            file_handler.write("{}\n".format(item))


def SearchNewFiles():
    '''Search for all files created or modified in a specific directory and within a timeframe that the user specifies'''

    # Getting the directory to scan from argv[1]
    DirToScan = sys.argv[1]

    # Getting the time interval from argv[2]
    time_interval = int(sys.argv[2])

    PrintOrSave = sys.argv[3]

    # Create a list to hold files if the user want to
    FilesList = []

    # prepare time variable to do the scan
    now = dt.datetime.now()
    ago = now-dt.timedelta(minutes= int(time_interval))

     
    # Loop through all directories and files within the directory
    # specified by the user and display all the files created
    # or modified within that period. 
    for root,dirs,files in os.walk(DirToScan):
        for fname in files:
            path = os.path.join(root, fname)
            st = os.stat(path)
            mtime = dt.datetime.fromtimestamp(st.st_mtime)
            if mtime > ago:
                # user chooses to display information in the screen 
                if PrintOrSave == 'P':
                    print('%s modified %s'%(path, mtime))
                # user chooses to save information to a file 
                elif PrintOrSave == 'S':
                    FilesList.append(path)
                    ListToFile(FilesList)
                else:
                    print "No files created or modified within the last " + time_interval +" minutes!"



def main():
    SearchNewFiles()

if __name__ =="__main__":
    main()



