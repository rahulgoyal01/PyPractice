#values in list called items
#values are stored under index, index are interger value.
#index starts at 0. from last it start from -1.

spam = ['cat', 'dog', 'tiger', 'elephant']
print(spam[-1::])
print(spam[0:2:])
print(spam[0::2])
print(spam[1::])
print(spam[:1:])

print("----------------------------------")

pam = [['cat','dog'],[1,2,3,4,5,6]]
print(len(pam[1]))
print(pam[0][1])
print(pam[1][3])
print("Rahul has " + str(pam[1][1]) + " " + pam[0][1])

print("----------------------------")

eggs = [10,20,30,40]
print(eggs)
eggs[3] = 'where'
print(eggs)

print("------------------------------")

#deleting index items
color = ['red','white','black']
del color[1]
print(color)

print("------------------------------")

# concat work same as strings
new_list = eggs + spam
print(new_list)

print("------------------------------")

# list function
func = list('hello')
print(func)

#boolean
print(3 in eggs)
print('red' in color)
