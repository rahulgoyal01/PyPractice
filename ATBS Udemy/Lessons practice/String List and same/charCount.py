import pprint

msg = "This is a bright summer day. Everthing supposed to go fine"
count = {}

for char in msg:
    count.setdefault(char, 0)
    count[char] += 1

print(count)
pprint.pprint(count)
