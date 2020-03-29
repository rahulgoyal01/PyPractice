# sub() is for subtitue, to print or show or replace a part of string.

import re
secret = 'Agent Robin give the secret documents to Agent Bob.'
nameRegex = re.compile(r'Agent \w+')
print(nameRegex.sub('REDSTAR', secret))
