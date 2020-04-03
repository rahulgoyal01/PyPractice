import re, pyperclip

# use this text https://automatetheboringstuff.com/files/examplePhoneEmailDirectory.pdf

# TODO : create a Regex for Phone number

phoneRegex = re.compile(r'''
#415-555-000,555-0000,(415) 555-0000,555-0000 ext 12345, ext. 12345, x12345)
(
((\d\d\d) | (\(\d\d\d\)))?   # area code optional
(\s | -)                    # first separator
\d\d\d                      # first 3 digits
-                           # separator
\d\d\d\d                    # last 4 digits
(((ext(\.)?\s) | x)         # extension word part(OPT)
(\d{2,5}))?                # extension num part(OPT)
)''', re.VERBOSE)
# TODO: Create a Regex for email address

emailRegex = re.compile(r'''
# some.+_thing@(\d{2,5})?.com

[a-z0-9_.+]+    # name part
@               # @ symbol
[a-z0-9_.+]+    # domain name part

''', re.VERBOSE | re.I)

# TODO: Get the text off the clipboard

text = pyperclip.paste()

# TODO: extract the email/phone from text
extractphn = phoneRegex.findall(text)
extractmail = emailRegex.findall(text)

print(extractmail)
#print(extractphn)

allphnNumber = [number[0] for number in extractphn] # Single line of code
#for number in extractphn:
#    allphnNumber.append(number[0])

print(allphnNumber)

# TODO: copy the extracted enmail/phone to the clipboard

    # useing join, we can join all phone numbers in a line instead of list

result = '\n'.join(allphnNumber) + '\n' + '\n'.join(extractmail)

pyperclip.copy(result)
