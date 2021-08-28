'''
Assume s is a string of lower case characters.

Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', your program should print:

Number of vowels: 5

'''

s = 'azcbobobegghakl' #Don't incluse this in the problem set ide.
num_vowels = 0
for x in s:
    if (x=='a' or x=='e' or x=='i' or x=='o' or x=='u'):
        num_vowels +=1
print('Number of vowels: ',num_vowels)
        