"""
Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your program should print

Longest substring in alphabetical order is: beggh
In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print

Longest substring in alphabetical order is: abc

"""

s = 'azcbobobegghakl'

#create an empty string to hold substrings
# iterate over the string
#Compare neighbours
# if neighbour 1 < neighbour 2, then they are in alphabetical order
#store value
# is your current substring longer than the previous ones?
# if not in order, there is no alphabetical substring.


empty_sub = ''
long_string = ''

for x in range(len(s)):
    if x == 0:
        empty_sub = s[x]
    elif s[x] >= s[x-1]:
        empty_sub+= s[x]
    else:
        empty_sub = s[x]
        
    if len(empty_sub) > len(long_string):
        long_string = empty_sub

print('Longest substring in alphabetical order is:',long_string)     
