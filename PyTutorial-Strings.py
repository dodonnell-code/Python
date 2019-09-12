# https://www.youtube.com/watch?v=k9TUPpGqYTo&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=2

message = 'hello world'
# Text can be enclosed in ' or " depending on what is in the string

message_test = '''Multiple
Lines
Of Text'''
# If the string spans multiples lines it should be enclosed in ''' or """

print(message)

print(message_test)

print(len(message))
print(message[0])
print(message[10])

print(message[0:5])
# first index is inclusive, second index is NOT

print(message[:5])
# if you leave out the first index Python will assume the beginning of the string

print(message[6:])
# if you leave off the last index Python will assume the end of the string

#String methods----------------------------


print(message.lower())
# change string to all lowercase--------------

print(message.upper())
# change string to all uppercase--------------

print(message.count('l'))
# count the number of times the selected character(s) occur in a string
#---------------------------------------------

print(message.find('l'))
# returns the index of the first instance of the character(s) in the string. If there is no instance it will return -1
#---------------------------------------------
message2 = 'Hello World'
print(message2)

message3 = message2.replace('World', 'Universe')
print(message3)
# assigns the replaced string to a new variable. The original does not change.

message2 = message2.replace('World', 'Universe')
print(message2)
# assigns the replaced string to the original variable. The original variable is now changed.
#-------------------------------

greeting = 'Hello'
name = 'Michael'

full_greeting = greeting + name
print(full_greeting)
#prints both variables with no space between

full_greeting = greeting + ', ' + name
print(full_greeting)
#prints variables with some formatting

full_greeting = '{}, {}. Welcome!'.format(greeting, name)
print(full_greeting)
#prints variables using a formatted string. {} is replaced with the variable names in order.

full_greeting = f'{greeting}, {name}. Welcome!'
print(full_greeting)
# new fstring. works in 3.6 and up. variables can call methods if desired (ie {name.upper})
#---------------------------------------------

print(dir(name))
#displays a list of methods available for a variable
#-------------------------------------------------------

print(help(str))
#displays the help file for a method
#-----------------------------------------




