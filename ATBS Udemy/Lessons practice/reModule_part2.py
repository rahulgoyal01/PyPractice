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


phnRegex = re.compile(r'(\d{3}-)?(\d{3}-\d{4})')
mo3 = phnRegex.findall('My new number is 555-0987 and 456-567-0000')
mo4 = phnRegex.search('My new number is 555-0987 and 456-567-0000')
print(mo3)
print(mo4.group())
