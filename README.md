# File Organizing Script

## Overview
This Python script organizes files in a specified directory by moving them into folders based on their file extensions. The script first checks if a folder corresponding to the file's extension exists. If it does, the file is moved into that folder. If not, the script creates a new folder for that extension and then moves the file into it.

## Requirements
- Python 3.x
- The `os` and `shutil` modules (these are part of Python's standard library)

## How to Use
1. Copy the script into a Python file, for example, `organize_files.py`.
2. Run the script and provide the path to the directory you want to organize when prompted.

## Script
```python
import os 
import shutil

Path = input("Enter the path: ")
files = os.listdir(Path)

for file in files:
    filename, extension = os.path.splitext(file)
    extension = extension[1:]
    
    if os.path.exists(Path + '/' + extension):
        shutil.move(Path + '/' + file, Path + '/' + extension + '/' + file)
    else:
        os.makedirs(Path + '/' + extension)
        shutil.move(Path + '/' + file, Path + '/' + extension + '/' + file)
