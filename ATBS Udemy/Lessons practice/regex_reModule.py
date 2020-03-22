import re

message = "Call me on 426-847-9898 or my personal cell 222-909-9999"

phnRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phnRegex.search(message)
print(mo.group()) #match object

#search method will look into the string for the
#specified pattern

#Compile function creates a regex object.

#group method, ties the finding as a single object
# use of parenthesis will divide then into groups

grpRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
num = grpRegex.search(message)
print(num.group(1)) # prints the area code
print(num.group(2))


phnRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo1 = phnRegex.findall(message)
print(mo1)

# findall returns all the number in a string
# in a list

#Pipe character

batRegex = re.compile(r'Bat(man|mobile|copter|bike)')
mo = batRegex.search('Batman has a batmobile and batcopter.')
print(mo.group()) 
