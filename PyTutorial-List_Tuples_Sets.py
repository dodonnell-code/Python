# https://www.youtube.com/watch?v=W8KRzm-HUcc&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=4
# LISTS = []
# TUPLES = ()
# SETS = {}

#To create an empty list, tuple, or set
# list = [] or list = list()
# tuple = () or tuple = tuple()
# set = set() >>> YOU CANNOT USE set = {}. this would create a dictionary
#---------------LISTS------------------------------
courses = ['History', 'Math', 'Physics', 'CIS']
print(courses) #prints the full list
print(len(courses)) #prints the length of the list
print(courses[2]) #prints slices
print(courses[1:2]) #prints slices
print(courses[:2]) #prints slices
print(courses[2:]) #prints slices
print(courses[-1]) #prints the last item in the list

courses.append('Art') #adds an item to the end of a list.
# if you add another list, it will add a list, not individual items. use extend to add items in a list to another list.

courses.insert(0, 'Science') #adds an item to a list at the specified index

print(courses)

courses2 = ['Gym', 'Lunch']
courses.extend(courses2) #adds items in a list to another list

print(courses)

courses.remove("Math") #removes the item named from the list
print(courses)

courses.pop() #removes the last item from the list
print(courses)

popped = courses.pop() #removes the last item in a list and assigns it to a variable
print(courses)
print(popped)

courses.reverse() #reverses the order of the values in the list
print(courses)

courses.sort() #sorts the list alphabetically or numerically based on type
print(courses)

courses.sort(reverse=True) #sorts the list alphabetically or numerically based on type
print(courses)

sortedC = sorted(courses) #returns a sorted version of the list but does NOT change the actual list order.
print(sortedC)

nums = [1,3,5,4,3]
print(min(nums)) #returns minimum value in a list
print(max(nums)) #returns max value in a list
print(sum(nums)) #returns the sum of values in a list


courses = ['History', 'Math', 'Physics', 'CIS']
print(courses.index('Math')) #returns the index of a named item

print("Art" in courses) #returns True or False based on list contents

for index, course in enumerate(courses): #loops through list and returns index number and item
    print(index, course)


for index, course in enumerate(courses, start=1): #loops through list and returns index number (starting at 1 instead of 0) and item
    print(index, course)

course_str = ', '.join(courses) #turns a list into a string with a named separator
print(course_str)

new_list = course_str.split(', ') #splits a str based on named separator and adds each item to a list
print(new_list)

#-----------------------TUPLES-----------------------------
#tuples CANNOT be modified like a list can
tuple1 = ('History', 'Math', 'Physics', 'CIS')
tuple2 = tuple1

print(tuple1)
print(tuple2)

#-----------------------SETS--------------------------
# Sets get rid of duplicates
# Sets can change order during run
# Used to determine membership in a group

course_list = {'History', 'Math', 'Physics', 'CIS'}
print(course_list)

art_courses = {'History', 'Design', 'Appreciation', 'Digital'}

print(course_list.intersection(art_courses)) #displays the list of items in set1 that are also in set2
print(course_list.difference(art_courses)) #displays the items in set1 that are not in set 2

print(course_list.union(art_courses)) #combine sets
