# https://www.youtube.com/watch?v=daefaLgNkw0&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=5

student = {'name':'John', 'Age':25, 'courses':['Math',
'CIS']}

print(student)
print(student['name'])
print(student['courses'])

print(student.get('phone')) #using the get method will return none instead of erroring out if a key isn't valid
print(student.get('phone', 'Not Found')) #using a default value will return the value instead of None if the key isn't valid

student['phone'] = '867-5309' #keys can be added this way
student['name'] = 'Jane' #values can be replaced this way

print(student)

student.update({'name': 'John', 'Age': 26, 'phone': '555-5555'}) #update method can be used to update/modify all key:value pairs at once
print(student)

del student['Age'] #keyword to remove a key pair
print(student)

student.update({'name': 'John', 'Age': 26, 'phone': '555-5555'})
print(student)
age = student.pop('Age') #removes age from the dictionary and assigns it to a variable
print(student)
print(age)

print(len(student)) #gets number of keys
print(student.keys()) #list keys in dictionary
print(student.values())

print(student.items()) #lists keys and their values

for key, value in student.items(): #loops must utilize items method
    print(key, value)
