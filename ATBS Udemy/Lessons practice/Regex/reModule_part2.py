import re

# ? is used to check for a part of string closed in
# parentesis to appear once or not at all

batRegex = re.compile(r'Bat(wo)?man')
mo = batRegex.search('The adventures of Batwoman')
print(mo.group())

mo1 = batRegex.search('The adventures of Batman')
print(mo1.group())

phnRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo2 = phnRegex.search('My ohone number is 899-999-2345')
print(mo2.group())

#ask stackoverflow
phnRegex = re.compile(r'((\d{3}-)?\d{3}-\d{4})')
mo3 = phnRegex.findall('My new number is 555-0987 and 456-567-0000')
mo4 = phnRegex.search('My new number is 555-0987 and 456-567-0000')
print(mo3)
print(mo4.group())

#

phoneRegex = re.compile(r'((\d\d\d-)?\d\d\d\-\d\d\d\d(,)?){3}')
mo5 = phoneRegex.search("my number are 123-123-3434,323-545-9999,090-878-6666.")
print(mo5.group())
print(mo5)

#The below is a greedy match, that means picking up 5
#character to match with the input string

haRegex = re.compile(r'(\d){3,5}') #min and max value
ha = haRegex.search("012345678910")
print(ha.group())

#{3,5}? turns it into a non-greedy match , picking small Value
