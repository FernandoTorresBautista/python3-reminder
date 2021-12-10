#!/usr/bin/python3
dict = {"Name":"Zara", "Age": 27, "Class":"First"}
print(dict)
print("Name: ", dict["Name"])
print("Age: ", dict["Age"])
input()
#update
dict["Age"] = 22
dict["School"] = "X School" # add new entry
print("Age: ", dict["Age"])
print("School: ", dict["School"])
input()
#delete
del dict["School"] #remove one entry
print("after delete School: ", dict)
dict.clear() # remove all entries
print("after clear dict: ", dict)
del dict #deleting entire dictionary
