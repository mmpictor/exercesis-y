#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 18:08:15 2018

@author: MASTER
"""

#The parameter weekday is True if it is a weekday, 
#and the parameter vacation is True if we are on vacation.
# We sleep #in if it is not a weekday or we're on vacation.
# Return True if we sleep in.

#write a function sleep_in which take two arguments bool 
def sleep_in(weekday, vacation):
    #we are flipping the bool value 
    if not weekday or vacation:
#    if weekday == False or vacation == True:
        return True
    else:
        return False 
x = sleep_in(True,False)
print(x)

#Given a string and a non-negative int n, 
#return a larger string that is n copies of the original string.

#string_times('Hi', 2) → 'HiHi'
#string_times('Hi', 3) → 'HiHiHi'
#string_times('Hi', 1) → 'Hi'

def string_times(str, n):
    return str * n 
a = string_times(4, 4)
print(a)



#Given a string name, e.g. "Bob",
# return a greeting of the form "Hello Bob!".


#hello_name('Bob') → 'Hello Bob!'
#hello_name('Alice') → 'Hello Alice!'
#hello_name('X') → 'Hello X!'

def hello(name):
    return 'Hello ' + name + '!'
b = hello('bob')
print(b)

#Given an array of ints, 
#return True if 6 appears as either 
#the first or last element in the array. The array will be length 1 or more.


#first_last6([1, 2, 6]) → True
#first_last6([6, 1, 2, 3]) → True
#first_last6([13, 6, 1, 2, 3]) → False

def first_last6(nums):
    if nums[0] == 6 or nums[-1] == 6:
        return True 
    else: 
        return False
    
a1 = first_last6([1, 2, 6])
print(a1)



#Given a string, return a string 
#where for every char in the original, there are two chars.
#
#
#double_char('The') → 'TThhee'
#double_char('AAbb') → 'AAAAbbbb'
#double_char('Hi-There') → 'HHii--TThheerree'

def double_char(str):
    #initialize a new string / empty
    to_return = ''
    for x in str:
        #add that character to return 
        to_return += x * 2
    return to_return
d = double_char('the')
print(d)

#Return the number of even ints in the given array.
# Note: the % "mod" operator computes the remainder, e.g. 5 % 2 is 1.


#count_evens([2, 1, 2, 3, 4]) → 3
#count_evens([2, 2, 0]) → 3
#count_evens([1, 3, 5]) → 0

def count_evens(nums):
    total = 0
    for x in nums:
        if x % 2 == 0:
            total += 1
    return total 

e = count_evens([2, 1, 3, 4])
print(e)













    