import sys

path=sys.argv[1]

def clearfolder(fpath):
    for the_file in os.listdir(fpath):
        file_path = os.path.join(fpath, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path): shutil.rmtree(file_path)
        except Exception as e:
            print(e)
            
if __name__ == '__main__':

     clearfolder(path)
