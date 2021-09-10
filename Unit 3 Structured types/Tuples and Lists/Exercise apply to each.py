# -*- coding: utf-8 -*-
"""

Here is the code for a function applyToEach:

def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])
Assume that

testList = [1, -4, 8, -9]
For each of the following questions (which you may assume is evaluated independently of the previous questions, so that testList has the value indicated above), provide an expression using applyToEach, so that after evaluation testList has the indicated value. You may need to write a simple procedure in each question to help with this process.

Example Question:

>>> print(testList)
[5, -20, 40, -45]
Solution to Example Question

def timesFive(a):
    return a * 5

applyToEach(testList, timesFive)
  >>> print(testList)
  [1, 4, 8, 9]
"""

def positive(var):
    return abs(var)
applyToEach(testList, positive)

'''
Exercise: apply to each 2
>>> print(testList)
  [2, -3, 9, -8]
'''
def addOne(a):
        return a + 1

applyToEach(testList, addOne)

'''
Exercise: apply to each 3

>>> print testList
  [1, 16, 64, 81]
'''
def squared(b):
    return b**2

applyToEach(testList, squared)


