#!/usr/bin/python3
import random
#choice() function
print("random number from range(100): ", random.choice(range(100)))
list=[1,2,3,5,9]
print("random element from a list: ", random.choice(list))
str="Hello world"
print("random character from string: ", random.choice(str))

#randrange() function
print("randrange(1,100,2): ", random.randrange(1,100,2))
print("randrange(100): ", random.randrange(100))

#random() function
# First random number
print("random(): ", random.random())
# Second random number
print("random(): ", random.random())

#seed() function
random.seed()
print("random number with default seed: ", random.random())
random.seed(10)
print("random number with int seed: ", random.random())
random.seed("hello", 2)
print("random number with string seed: ", random.random())

#suffle() frunction
list=[20,16,10,5]
random.shuffle(list)
print("Reshuffled list: ", list)

random.shuffle(list)
print("Reshuffled list: ", list)

#uniform() function
print("Random Float uniform(5,10): ", random.uniform(5,10))

print("Random Float uniform(7,14): ", random.uniform(7,14))
