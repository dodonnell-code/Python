# https://www.youtube.com/watch?v=khKv-8q7YmY&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=3

num = 3
print(type(num))

num = 3.14
print(type(num))

print(3+2) #addition
print(3-2) #subtraction
print(3*2) #multiplication
print(3/2) #division
print(3//2) #floor division (drops decimal)
print(3**2) #exponent
print(3%2) #modulous (shows remainder, always 0 or 1)


num = 1
num = num + 1
print(num)

num =1
num += 1 #same operation as num = num + 1
print(num)

num = 2
num *= 10
print(num)

print(abs(-3)) #absolute value
print(round(3.75)) #rounds to the nearest whole number
print(round(3.75,1)) #rounds to the nearest decimal place indicated by the second input.

#Comparators: Always returns True or False
#Equal: ==
#Not Equal: !=
#Greater Than: >
#Less Than: <
#Greater or Equal: >=
#Less or Equal: <=

num1 = 3
num2 = 2

print(num1 == num2)
print(num1 != num2)
print(num1 > num2)
print(num1 < num2)
print(num1 >= num2)
print(num1 <= num2)

#How to deal with numbers that COULD be strings
num_1 = '100'
num_2 = '200'
print(num_1 + num_2)

num_1 = int(num_1)
num_2 = int(num_2)
print(num_1 + num_2)
