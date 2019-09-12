# https://www.youtube.com/watch?v=6iF8Xb7Z3wQ&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=8&t=0s

nums = [1,2,3,4,5]

for num in nums:
    if num == 3:
        print('Found!')
        break #this will force the loop to stop
    print(num)

for num in nums:
    if num == 3:
        print('Found!')
        continue #this will skip the rest of the iteration and continue the for loop
    print(num)

for num in nums:
    for letter in 'abc':
        print(num, letter) #gives every combination of numbers from list and letters abc

for i in range(10):  #use to loop x times as indicated by range value.
    print(i)

for i in range(1,11): #you can determine the starting value using additional parameters in range n - n-1
    print(i)

x=0
while x < 10: #loops until the condition is met.
    print(x)
    x+=1 #make sure to increment so that the loop isn't infinite

x=0
while x < 10: #loops until the condition is met.
    if x == 5:
        break
    print(x)
    x+=1 #make sure to increment so that the loop isn't infinite

x=0
while True: #this will loop forever until it hits the break point
    if x == 5:
        break
    print(x)
    x += 1

