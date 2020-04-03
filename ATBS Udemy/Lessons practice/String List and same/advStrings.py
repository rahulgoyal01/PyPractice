# escape character \ followed by special char you add into string

print("that is Alice's cat")
print('Say hi to Bob\'s mother')
print('hello there\nSay hi\t to Bob\'s mother')

#triple quote

print("""hi there,
what are you up to? Should we go out some day.
lets catch up""")

#Indexes, Slices, in and not in all works with strings as it with list.
spam = "hello World"

print("Hello" in spam)

# String methods, lower() and upper()

print(spam.lower())
print(spam.upper())

# isupper() and islower() returns boolean value checking the sting is lower or upper.

print(spam[:5].upper().isupper())

#other boolean are isalpha, isalnum, istitle, isdecimal and isspace

print(spam.isalnum()) #contain one white space
print(spam[:5].isalpha())
print(spam[5].isspace())

#startswith(), endswith()
# join() use with list and strings
print('\t'.join(spam))

# rjust() and ljust() adds spaces to match the length passed in the method
# centre(), place text in centre filling the rest with empty space or another character

print(spam.center(30, '='))

#strip() removes the character passed from a string, spaces if empty present
# on either sides of a string. similarly, rstrip and lstrip
print('  spam  '.strip())
print('dghftiewafklndslcirdfgt'.strip('dfgt'))

#replace()

print(spam.replace('l','NEW'))
