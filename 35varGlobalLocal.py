#!/usr/bin/python3

total = 0 #global variable

#funtion definition
def sum(arg1,arg2):
    "Add both the parameters and return them"
    total = arg1 + arg2
    print("inside the function local total: ", total)
    return total

#now you can call sum function
sum(10,20)
print("outside the function flobal total: ", total)
