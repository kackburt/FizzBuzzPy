
#-*- coding: utf-8 -*-

print("Welcome to fizzbuzz!")
userinput = int(raw_input("Please enter a number between 1 and 100: "))

for i in range(1,userinput+1):
    if i % 3 == 0 and i % 5 == 0:
        print("fizzbuzz")
    elif i % 3 == 0:
        print("fizz")
    elif i % 5 == 0:
        print("buzz")
    else:
        print i