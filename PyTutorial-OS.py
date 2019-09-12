# https://www.youtube.com/watch?v=tJxcKyFMTGo&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=23

import os #import from standard library
from datetime import datetime

#print(dir(os)) #print list of attributes and methods from module
print(os.getcwd()) #get current working directory

os.chdir('C:/Users/dodonnell/Desktop') #change the working directory
print(os.getcwd())
'''
print(os.listdir()) #list all files in current directory

os.mkdir('OS-Demo-1') #will only create one level
os.makedirs('OS-Demo-2/sub1') #will create multiple levels

os.rmdir('OS-Demo-1') #removes one directory
os.removedirs('OS-Demo-2/sub1') #removes directory and all sub directories

os.rename('test.txt', 'test2.txt') #renames a file or folder

print(os.stat('test2.txt')) #prints our file attributes
print(os.stat('test2.txt').st_mtime) #displays just the attribute selected

mod_time = os.stat('test2.txt').st_mtime #pulls last modified date
print(datetime.fromtimestamp(mod_time))  #diplays timestamp in readable format

for dirpath, dirnames, filenames in os.walk(os.getcwd()): #traverses path from top down
    print('Current Path: ', dirpath)
    print('Directories: ', dirnames)
    print('Files: ', filenames)
    print()


filepath = os.path.join(os.getcwd(), 'test.txt') #combines 2 paths to generate a usable filepath.
print(filepath)

'''
print(os.path.basename('tmp/test.txt')) #gives just the filename
print(os.path.dirname('tmp/test.txt')) #gives just the directory
print(os.path.split('tmp/test.txt')) #gives both as separate items in a list

print(os.path.exists('tmp/test.txt')) #checks if a path exists
print(os.path.isdir('tmp/test.txt')) #checks if a path exists as a directory
print(os.path.isfile('tmp/test.txt')) #checks if a path exists as a file

print(os.path.splitext('tmp/test.txt')) #split the file name(path) and extension


