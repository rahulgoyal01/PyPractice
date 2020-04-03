# findall method examples

import re

phnRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
resume = ''' these are the list of numbers from the directory. 123-123-5555
         345-413-4949, 345-332-4554, 222-222-0000 and 234-456-4343.
         Oh! I missed one more 440-440-3989.'''

print(phnRegex.search(resume)) # give only first occurence
print(phnRegex.findall(resume)) # provide list of numbers matching the pattern

phnRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
#retrun a list of tuples as we have 2 groups now to match
print(phnRegex.findall(resume))

# \d = [0|1|2|3|4|5|6|7|8|9], any numeric digit
# \D = any char except numeric simply not \d
# \w = any char # \W = not any char
# \s = any space, tab or new line # \S = not \s

lyrics = '12 d d, 11 p p, 10 l l, 9 l d, 8 m m'

xmasRegex = re.compile(r'\d+\s\w+')
print(xmasRegex.findall(lyrics))

#print out vowles in the given string
vwlRegex = re.compile(r'[aeiou]', re.I) #re.I is used for case insensitive
print(vwlRegex.findall('This is a stone having lots of vowels.'))

#print out consonant in the given string, ^ used for not here, not aeiou
# including punctuation mark and spaces.
consonantRegex = re.compile(r'[^aeiou]', re.I)
print(consonantRegex.findall('This is a stone having lots of vowels.'))
