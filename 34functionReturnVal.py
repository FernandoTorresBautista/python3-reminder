#!/usr/bin/python3

#Function definition
def sum(arg1, arg2):
    "add both the parameters and return them."
    total = arg1 + arg2
    print("inside the function: ", total)
    return total

#Now you can call the function
total = sum(10,20)
print("outside the function: ", total)
