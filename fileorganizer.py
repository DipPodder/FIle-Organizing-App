import os 
import shutil

Path = input("Enter the path: ")
files = os.listdir(Path)

for file in files:
    filename,extension = os.path.splitext(file)
    extension = extension[1:]
    
    if os.path.exists(Path+'/'+extension):
        shutil.move(Path+'/'+file,Path+'/'+extension+'/'+file)
    else:
        os.makedirs(Path+'/'+extension)
        shutil.move(Path+'/'+file,Path+'/'+extension+'/'+file)