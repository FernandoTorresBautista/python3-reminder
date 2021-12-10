#!/usr/bin/python3

#conditional if/else/elseif

#if
discount=0
amount=int(input("Enter amount: "))
if amount > 1000:
    discount=amount*0.10
print("Discount: ", discount)
print("Net amount : ", amount-discount,"\n")

#if else
if amount > 1000:
    discount=amount*0.10
else:
    discount=amount*0.05
print("Discount: ", discount)
print("Net amount : ", amount-discount,"\n")

#if elseif else 
if amount > 1000:
    discount=amount*0.10
elif amount > 500:
    discount=amount*0.05
else:
    discount=0
print("Discount: ", discount)
print("Net amount : ", amount-discount)
