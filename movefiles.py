import sys
import os
import shutil

inputfolder = sys.argv[1]
outputfolder = sys.argv[2]


def moveFiles(inputfolder, outputfolder):
    
    infiles = os.listdir(inputfolder)

    for f in infiles:
        shutil.move(inputfolder+f, outputfolder)


if __name__ == '__main__':

     moveFiles(inputfolder, outputfolder)