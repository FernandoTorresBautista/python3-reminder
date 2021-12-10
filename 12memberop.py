#!/usr/bin/python3

a = 10
b = 20
list = [1,2,3,4,5]
print(list)
print("a=",a,", b=",b)
if (a in list):
    print("Line 1 - a is available in the given list")
else:
    print("Line 1 - a is not available in the given list")

if (b not in list):
    print("Line 2 - b is available in the given list")
else:
    print("Line 2 - b is not available in the given list")

c = 2
print("c=",c)
if (c in list):
    print("Line 3 - c is available in the given list")
else:
    print("Line 3 - c is not available in the given list")
