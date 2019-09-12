# https://www.youtube.com/watch?v=CqvZ3vGoGs0&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=10&t=0s

'''
There are several ways to import a module
------------Modules in the same directory--------------------
import my_module - this will import and run the whole module on load
    my_module.find_index(courses, "Math")

import my_module as mm - this will import the module with an alias (for easier typing)
    mm.find_index(courses, "Math")

from my_module import find_index - this will only import the function find_index from my_module.
    You do NOT neet to call the module this way.
    find_index()

from my_module import find_index, test - this will only import the objects specified from my_module.
    You do NOT neet to call the module this way.
    find_index()
    test

from my_module import find_index as fi, test - aliases can also created using this method.
    fi()

from my_module import * - this can be used but is frowned upon as it can make code confusing.

------------Modules in a different directory--------------------
BEST PRACTICE SAYS TO USE A PACKAGE but you can do this
import sys - insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, '/path/to/application/app/folder')

import module
'''
from my_module import find_index as fi, test #import find_index with an alias and the variable test. Nothing else will be imported.
import random #imports random from the standard library
import datetime
import calendar
import os #gives access to operating system
import webbrowser

courses = ['History', 'Math', 'Physics', 'CompSci']

print(fi(courses, "Math"))

random_course = random.choice(courses)
print(random_course)

today = datetime.date.today()
print(today)

print(calendar.isleap(2020))

print(os.getcwd())

print(os.__file__) #prints out the location of the file

#webbrowser.open("https://www.mcccu.org")
