# list are mutable, that means the data they hold can be altered with.
# data in a list are stored in a refrence no.
# if a list is assigned to other variable then any change to the second
# variable will cause a change in 1st variable.

spam = [1,2,3,4,5]
eggs = spam
print(eggs)
eggs[3] = 'Hello'
print(spam)
