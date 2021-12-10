#!/usr/bin/python3

for letter in "Python": #first example
    if letter == "h":
        continue
    print("Current letter:", letter)

var = 10 #second example
while var>0:
    print("Current variable value: ", var)
    var += -1
    if var == 5:
        continue

pwd = "123" #third example
while(True):
    x=input("password: ")
    if x != pwd:
        print("enter again...")
        continue
    print("password entered correctly")
    break
