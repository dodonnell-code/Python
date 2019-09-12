#https://www.youtube.com/watch?v=Uh2ebFW8OYM&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=26&t=0s

'''
r: read
w: write
a: append
r+: read and write

'''
f = open('C:/users/dodonnell/desktop/test2.txt', 'r')

print(f.name)
print(f.mode)
f.close() # you must explicitly close a file opened with open()

'''opening a file in a context manager is a better way to open files

'''
with open('C:/users/dodonnell/desktop/test2.txt', 'r')  as f:
    '''
    This is the same as above, only safer.
    File will automatically close and will also close if there is an exception
    '''
    #print(f.name)
    #print(f.mode)

    #f_contents = f.read() #assign contents of file to a variable
    #print(f_contents)

    #f_lines = f.readlines() #assign contents of a file to a list
    #print(f_lines)

    '''
    f_line = f.readline() #assign the contents of 1 line to variable
    print(f_line)
    f_line = f.readline() #each time this method is used it pulls the next line into the variable.
    print(f_line)
    f_line = f.readline()
    print(f_line, end = '')
    f_line = f.readline() #add end='' to remove the newline
    print(f_line, end = '')


    for line in f:
        print(line, end = '')  #same as above but more efficient


    x = 10
    f_contents = f.read(x) #reads only first x characters in the file
    while len(f_contents) > 0:
        print(f_contents, end = '')
        f_contents = f.read(x)
        #print(f.tell()) #show position of cursor in file


    '''
'''
with open('C:/users/dodonnell/desktop/test.txt', 'w')  as f:
    f.write('test') #write to a file
    f.seek(0) # used to change position of cursor
    f.write('b')


with open('C:/users/dodonnell/desktop/test.txt', 'r')  as rf:
    with open('C:/users/dodonnell/desktop/test2.txt', 'w')  as wf:
        for line in rf:
            wf.write(line)
'''
#images must be opened in binary mode
with open('C:/users/dodonnell/desktop/test.jpg', 'rb')  as rf: #add a b to the file operation flag
    with open('C:/users/dodonnell/desktop/test2.jpg', 'wb')  as wf:
        chunk_size = 4096 #set the chuck size to read. similiar to character number flag
        rf_chunk = rf.read(chunk_size)
        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)
