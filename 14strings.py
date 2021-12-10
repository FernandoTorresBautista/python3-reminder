#different ways to define a string in Python
str1 = 'welcome'
print(str1)

str2 = "welcome"
print(str2)

str3 = '''welcome'''
print(str3)

str = """welcome
to the world of python"""
print(str)

# accessing characters in a string
mystr = 'language'
print("mystr: ", mystr)

print("mystr[0]", mystr[0])
print("mystr[-1]", mystr[-1])
print("mystr[1:5]", mystr[1:5])
print("mystr[5:-2]", mystr[5:-2])

#different strings can be assigned
mystr = "programming"
print("mystr: ",mystr)

# concatenation
print("mystr + str1: ", mystr + str1)
print("mystr *3 : ", mystr * 3)

#iterating
letter_count = 0
for letter in 'Hello ':
    if (letter == "l"):
        letter_count+=1
print(letter_count, " times l letter has been found")

#menbership
print("l" in  "Hello")
print("l" not in  "Hello")
print("b" in  "Hello")
print("b" not in  "Hello")

#built-in functions
mystr = "university"

# using enumerate()
my_list_enumerate = list(enumerate(mystr))
print("list(enumerate(mystr)): ", my_list_enumerate)

#using character count
print("len(mystr): ", len(mystr))

print("C:\\User\\user\\mydata.txt")
print("this line is having a new line \ncharacter")
print("this line is having a tab \t character")
print("ABC written in \x42\x42\x43 (HEX) representation")

# format() method
#default implicit
default_order = "{} {} and {}".format("Today","is","Sunday")
print(default_order)

#order using positional arguments 
positional_order = "{1} {0} and {2}".format("is","Today","Sunday")
print(positional_order)

#order using keyword argument
keyword_order = "{t} {i} and {s}".format(i="is",t="Today",s="Sunday")
print(keyword_order)

#formatting numbers
print("required binary representation of {0} is {0:b}".format(20))

#formatting floats
print("Exponent representation: {0:e}".format(1566.345))
name = 'xyz'
print("welcome %s" %name)
age = 25
print("age = %d" %age)
print("age is %s" %age)
marks = 55
print("marks=%f" %marks)

print("age in octal %o" %age)
print("age in hexadecimal %x" %age)
print("age with exp %e" %age)

# round off
print("one third is: {0:.3f}".format(1/3))

#string methods
print("GooD morNIng tO alL".lower())
print("GooD morNIng tO alL".upper())
print("GooD morNIng tO alL".find('tO'))
print("GooD morNIng tO alL".find('to'))
print("GooD morNIng tO alL".replace('alL', "everybody"))
print("GooD morNIng tO alL".replace('all', "everybody"))

#
