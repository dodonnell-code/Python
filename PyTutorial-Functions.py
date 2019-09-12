#https://www.youtube.com/watch?v=9Os0o3wzS_I&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=8

def hello_func(): #define a function. () is for parameters
    """Doc Strings should be used to explain a function"""
    pass # keyword used to prevent errors from an empty function

hello_func() #use the function name to call a function

def hello_func2():
    print('This is a function')

hello_func2()

for i in range(4): #calls the function i number of times
    hello_func2()

def hello_func3():
    return "Hello Functions!" #returns a value to the calling program

print(hello_func3())
print(hello_func3().upper()) #you can use other methods on returned strings

def hello_func4(greeting): #you can assign inputs for the method
    return '{}, user'.format(greeting) #and return them here

print(hello_func4('Welcome')) #if an input is listed in the method (without a default value), input must be passed to call the method

def hello_func5(greeting, name = "User"): #if a default value is used, the argument doesn't have to be passed
    return '{}, {}'.format(greeting, name)

print(hello_func5("Welcome", "Dan")) #passing an argument will use the argument
print(hello_func5("Welcome")) #not passing the argument will use the default


def student_info(*args, **kwargs): #*args and **kwargs allow an arbitratry number of positional or keyword arguments
    #name isn't important BUT are the conventional names used for this type of argument
    #args = arguments
    #kwargs = keyword arguements
    print(args)
    print(kwargs)

student_info('Math', 'Art', name = "Jon", age = 22)

courses = ['Math', 'Art']
info = {'name': 'John', 'age': 22}

student_info(courses, info) #doing this will pass the list and dictionary as positional arguments NOT individual arguments

student_info(*courses, **info) #this will unpack and pass the arguements individually

#-------------------------EXAMPLE---------------------------------
month_days = [0,31,28,31,30,31,30,31,31,30,31,30,31]

def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(year, month): #test for a valid month
    if not 1 <= month <= 12:
        return "invalid month"

    if month == 2 and is_leap(year): #checks if month is Feb and a leap year (Calls is_leap())
        return 29

    return month_days[month] #returns the days in the submitted month

print(days_in_month(2020,2))
