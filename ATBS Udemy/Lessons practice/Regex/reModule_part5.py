# sub() is for subtitue, to print or show or replace a part of string.

import re
secret = 'Agent Robin give the secret documents to Agent Bob.'
nameRegex = re.compile(r'Agent \w+')
print(nameRegex.findall(secret))
print(nameRegex.sub('REDSTAR', secret))



nameRegex = re.compile(r'Agent (\w)\w+')
print(nameRegex.findall(secret))
# in the substitute string I want some part of the original string
print(nameRegex.sub(r'Agent \1*****', secret))


#compile supports indententaion for clean coding with re.VERBOSE
#helping to add spaces and comments

numRegex = re.compile(r"""
            (\d\d\d-)|  # area code without parens, with dash
            (\(\d\d\d\) ) # -or- area code with parens and no dash
            \d\d\d      # first 3 digits
            -           # second dash
            \d\d\d\d    # last 4 digits
            \sx\d{2,4}  # extension, like x1234
            """, re.VERBOSE)
