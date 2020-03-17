# loops and list
a = range(4)
print(a)
for i in a:
    print(i)
print("--------------------------------")

b = list(range(4))
print(b)

c = list(range(0,100,3))
print(c)
print("--------------------------------")

supplies = ['pens','paper','apple','flowers','dog-food']
for i in range(len(supplies)):
    print("item number " + str(i+1) + " is " + supplies[i])
print("--------------------------------")

# multiple assignment to list

cat = ['fat','orange','loud']
size, color, disposition = cat
print(size)
print("--------------------------------")
#swapping variables
a = 4
b = 'sdf'

a, b = b, a
print(a, b)

cat, supplies = supplies, cat
print(cat)
print("--------------------------------")
