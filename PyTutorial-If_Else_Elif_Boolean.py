#https://www.youtube.com/watch?v=DZwmZ8Usvnk&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=6

#Comparisons are the same as for numbers with the addition of
#Object Identity = is
#This checks to see if the items are the same in memory

#These items equate to False
#False
#0 of any numerical type
#any empty sequence (), [], ''
#any empty mapping {}


if True: #this will always happen
    print("Conditional was True")

if False: #this will never happen
    print("Conditional was False")


language = "Java"
if language == 'Python':
    print("Conditional was True")

if language == 'Python':
    print('Language is Python') #if true do this
else:
    print('No Match') #if false do this


if language == 'Python':
    print('Language is Python') #if first condition is true do this
elif language == 'Java':
    print('Language is Java') #if second condition is true do this
else:
    print('No Match') #do this if no conditions are true

user = "admin"
logged_in = True

if user == 'admin' and logged_in: #use AND keyword to test multiple criteria. logged_in can only be true or false and the condition will only pass if true so there is no need to say logged_in == True
    print('Admin Page')
else:
    print('Bad Creds')


if user == 'admin' or logged_in: #use OR keyword to test if any of the conditions are true
    print('Admin Page')
else:
    print('Bad Creds')

if not logged_in: #use NOT keyword to reverse true and false
    print('Log In')
else:
    print('Welcome')


a = [1, 2, 3]
b = [1, 2, 3]

print(a == b) #this is true because the values of a and b are the same
print(a is b) #this is false because a and b are not the same objects in memory

print(id(a)) #shows the memory location of a
print(id(b)) #shows the memory location of b
b = a

print(a == b) #this is true because the values of a and b are the same
print(a is b) #this is now true because a and b are the same object
print(id(a)) #shows the memory location of a
print(id(b)) #shows the memory location of b
#(a is b) is the same as (id(a) == id(b))



