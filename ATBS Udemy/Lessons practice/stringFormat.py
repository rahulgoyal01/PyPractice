#this is a example of string formatting where %s and %d are use for sting and
#number in the last print statment instead of the variable name and concat

print('Enter your name:', end='')
name = input()
print('Please enter your age:', end='')
age = int(input())

print("Hi %s, you are a young lad of age %d." % (name,age))
