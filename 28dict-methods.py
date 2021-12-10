#!/usr/bin/python3
#dictionary methods

#clear () method
dict0 = {'Name':'Zara','Age':22}
print("Start len: %d" % len(dict0))
dict0.clear()
print("End len: %d" % len(dict0))
input()

#copy () method
dict1 = {'subjects':['phy','che']}
dict2 = dict1.copy()
print("new dictionary: ", dict2)
dict2["subjects"].append("maths")
print("dict1: ", dict1)
print("dict2: ", dict2)
input()

#fromkeys () method
seq = ("name","age","sex")
dict3 = dict.fromkeys(seq)
print("New dictionary: ", dict3)
dict3 = dict.fromkeys(seq, 10)
print("New dictionary: ", dict3)
input()

#get () method
dict4 = {'Name':'Zara','Age':22}
print(dict4)
print("get('Age'): ", dict4.get("Age"))
print("get('Sex'): ", dict4.get("Sex"))
input()

#items() method
print("k-v pairs: ", dict4.items())
input()

#keys() method
dict5 = {"Name":"Rama","Age":7}
#print("list of keys: ", dict5.keys())
print("list of keys: ", dict4.keys())
input()

#values() method
print("values: ", dict4.values())
input()

#setdefault() method
dict5.setdefault("class",None)
dict5.setdefault("Age",100)
print(dict5)
input()

#update() method
dict6 = {'Name':'Zara','Age':22}
dict7 = {"sex":"female"}
print(dict6, dict7)
dict6.update(dict7)
print("updated dict6:", dict6)
