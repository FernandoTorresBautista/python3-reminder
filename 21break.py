#!/usr/bin/python3

for letter in "Python": #first example
    if letter == "h":
        break
    print("Current letter:", letter)
var = 10 #second example
while var>0:
    print("Current variable value: ", var)
    var += -1
    if var == 5:
        break
print("bye")
id = [1,2,3,4,5]
x = int(input("Enter a number: "))
for i in range(len(id)):
    if x == id[i]:
        break
if i<len(id)-1:
    print(x, " found at position: ",i+1)
else:
    print(x, " not found in list")
