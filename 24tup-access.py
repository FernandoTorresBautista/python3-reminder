#!/usr/bin/python3

tup1 = ('physics','checmistry',1997,2000)
tup2 = (1,2,3,4,5,6,7)
print(tup1, tup2)
print("tup1[0]: ", tup1[0])
print("tup2[1:5]: ", tup2[1:5])
input("continue")
# updating
print("update example")
tup1 = (12, 34.56)
tup2 = ('abc', 'xyz')
print(tup1, tup2)
# following action is not valid for tuples
#tup1[0] = 100 #does not support assignment 
# so let0s create a new tuple as follows
tup3 = tup1 + tup2
print("new tuple: ", tup3)
input("continue")
#delete
print("delete example")
tup = ('physics','checmistry',1997,2000)
print("before deleting: ", tup)
del tup
print("after deleting tup: ")
#print(tup)#there is not more 

# update & delete
