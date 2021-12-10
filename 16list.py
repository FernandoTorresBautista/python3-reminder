#!/usr/bin/python

#access, update & delete

#access
list1 = ["physics", "chemistry", 1997, 2000]
list2 = [1,2,3,4,5,6,7]
print("list1[0] ",list1[0])
print("list2[1:5] ",list2[1:5])

# update
print("value available at index 2: ", list1[2])
list1[2] = 2001
print("New value available at index 2: ", list1[2])

#delete
print(list1)
del list1[2]
print("After deleting value at index 2: ", list1)
del list2
#print(list2) # deleted

#operations
listx = ["abcd", 786, 2.23, "jhon", 70.2]
tinylist = [123, "jhon"]
print(listx, tinylist) # complete list
print(listx[0]) #zero index
print(listx[1:3]) #slice 1:3
print(listx[2:]) #slice 2:
print(tinylist * 2) #repeats list two times
print(listx + tinylist)

# object methods
# append, clear, copy, count, extend, index, insert, pop, remove, reverse, sort

#append
list1 = ["c++", "java", "python"]
list1.append("go")
print("updated list: ", list1)

#count
print("count list: ", list1.count("go"))
print("count list: ", list1.count("c++"))

#extend
list2 = ["js"]
list1.extend(list2)
print("extended list: ", list1)

#index
print("index of go :", list1.index("go"))
print("index of js :", list1.index("js"))

#insert
list1.insert(1,"r")
print("inserted r: ", list1)

#pop
obj = list1.pop() 
print("popped js: ", obj)
print("list : ", list1)

#remove
list1.remove("r")
print("removed r: ", list1)

#reverse
list1.reverse()
print("revert list: ", list1)

#sort
list1.sort()
print("sorted list: ",list1)


# built in list functions
#len, max, min, list(seq)
#len
print("length=", len(list1))

#max, min
list2=[456,700,300]
print("max=", max(list1))
print("max=", max(list2))

print("min=", min(list1))
print("min=", min(list2))

#list
aTuple = (123, "c++", "java", "python")
list1 = list(aTuple)
print("list1 elements: ", list1)

str = "Hello"
list2 = list(str)
print("list2 elements: ", list2)
