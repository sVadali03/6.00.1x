'''
Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', then your program should print

Number of times bob occurs is: 2
'''

s = 'azcbobobegghakl'

count_bob = 0

for x in range(len(s)+1):
    if s[x:x+3] == 'bob':
        count_bob +=1
print("Number of times bob occurs is:",count_bob)
    