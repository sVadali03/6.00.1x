"""
Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your program should print

Longest substring in alphabetical order is: beggh
In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print

Longest substring in alphabetical order is: abc

"""

s = 'azcbobobegghakl'

long = ''
substring = ''

for x in range(len(s)):
    if x==0:
        substring = s[x]
    elif s[x] >= s[x-1]:
        substring+= s[x]
    else:
        substring = s[x]
    
    if len(substring) > len(long):
        long = substring
print('Longest substring in alphabetical order is:',long)