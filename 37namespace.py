#!/usr/bin/python3

count=2000
def AddCount():
    # uncomment the following line to fix the code
    global count # use global to use the global variable 
    count = count + 1

print(count)
AddCount()
print(count)
