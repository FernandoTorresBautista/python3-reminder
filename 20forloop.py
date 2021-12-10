#!usr/bin/python3

# for loop 
for letter in "python":
    print("current letter: ", letter)

fruits = ["banana", "apple", "mango"]
for fruit in fruits:
    print("current fruit: ", fruit)

print("bye")

# for loop using range() function
print("range 3")
for num in range(3):
    print(num)

print("range start,stop")
for num in range(1,4):
    print(num)

print("range start, stop, step")
for num in range(1,6,2):
    print(num)

# for loop iterating by sequence index
dict = {"011":"New Delhi", "022":"Mumbai", "033":"Kolkata"}
for key in dict:
    print(dict[key])

for key, value in dict.items():
    print(key, value)

for value in dict.values():
    print(value)

for key in dict.keys():
    print(key)

#nested of for loops
for i in range(1,11):
    for j in range(1,11):
        k=i*j
        print(k, end=" ")
    print()

