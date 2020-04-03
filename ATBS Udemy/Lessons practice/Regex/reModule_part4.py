# Dot-Strt and the Caret/Dollar

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

atRegex = re.compile(r'.at') #looking for a single char before 'at'
print(atRegex.findall('The cat in the hat sat on the flat mat'))

nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)', re.I)
print(nameRegex.findall('First Name: Rahul Last name: Goyal'))

serve = '<To server humans> the dinner>'
nonGreedy = re.compile(r'<.*?>')  # r'<(.*?)>'
print(nonGreedy.findall(serve))

greedy = re.compile(r'<.*>') # r'<(.*)>'
print(greedy.findall(serve))

prime = 'Server the public trust.\nProtect the innocent.\nUplosd the law.'
dotstart = re.compile(r'.*')
print(dotstart.search(prime))

dotstart = re.compile(r'.*', re.DOTALL) # prints the whole line including new line char
print(dotstart.search(prime))
