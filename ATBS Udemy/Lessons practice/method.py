#using method with list

spam = ['hello','hi','howdy','hey','hi']
a = spam.index('hello')
print(a)
#if ther eare duplicate values then the index method will return only
#the first occurennce
print(spam.index('hi'))

print("--------------------------")
# adding data to list using append() and insert()
# only works with list kind of data type not strings and number
spam.append('dof')
print(spam)

spam.insert(2, 'new')
print(spam)

spam.remove('hey')
print(spam)

#sort method, doesnt work with mixed data in list, interger plus string
num = [11,2,34,6,0,-11]
color = ['red','brown','yellow','white']
color.sort()
print(color)
color.sort(reverse=True)
print(color)
num.sort()
print(num)

#sorting happens in "ASCII-betical" order. to sort normally, pass
#key=str.lower
