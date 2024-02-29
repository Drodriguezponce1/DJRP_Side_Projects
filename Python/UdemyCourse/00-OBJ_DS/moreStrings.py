myStr = "Hello World"

#indexing
    #grab a single letter in the string
print(myStr[2])

    #reverse indexing
print(myStr[-1])

#Slicing
myStr = "abcdefghi" 
    #substring
print(myStr[2:8])
    #From 0 up to but not including x
print(myStr[:3])
    #example for 'def'
print(myStr[3:6])
    #STEP (STARTING AT INDEX 0, OUTPUT EVERY OTHER INDEX) (0,2,4,6,8...)
print(myStr[::2])
    #BACKWORDS STEP
print(myStr[::-1])

#CODING PRACTICE:   write 1 line where it grabs the letter 'r' from 'Hello World'
myStr = 'Hello World'
print(myStr[8:9:1])
print(myStr[8])

#MORE PRACTICE : write 1 line to get 'ink' from 'tinker'
myStr = 'tinker'
print(myStr[1:4])