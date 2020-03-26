import re

beginRegex = re.compile(r'^Hello') #begin with expression ^
print(beginRegex.search('Hello There'))
print(beginRegex.search('He said "Hello!"')) # this returns consonantRegex

endRegex = re.compile(r'world$')
print(endRegex.search('Hello world'))

allDigitRegex = re.compile(r'\d+$')
print(allDigitRegex.search('This string contains he110 and 060393'))

allDigitRegex = re.compile(r'^\d+$')
print(allDigitRegex.search('329850275'))
