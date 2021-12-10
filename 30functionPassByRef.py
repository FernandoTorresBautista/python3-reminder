#!/usr/bin/python3

#Function definition
def changeme(mylist):
    "This changes a passed list into this function"
    print(id(mylist))
    print("Values inside the function before change: ", mylist)
    mylist[2]=50
    print("Values inside the function after change: ", mylist)
    return

# Now you can call changeme function
mylist = [10,20,30]
print(id(mylist))
changeme(mylist)
print("Values outside the function: ", mylist)

# arguments are required
# changeme() #fail
