#!/usr/bin/python3
#Function definition
def printinfo(name, age=35):
    "This prints a passed info into this function"
    print("Name:", name)
    print("Age:",age)
    return

#Now you call printinfo
printinfo("xyz")
printinfo(age=50,name="fer")
