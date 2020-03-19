
myDict = {'key1': 'Value1', 'key2': 'Value2',
           'key3': 'Value3'}

print("this is  " + myDict['key2'])

#dictionaries are mutable like list
#dict supports list(), value() and item() methods.
# item method returns dict key and value as tuple.

print(myDict.items())
print("-------------------------------------------")
myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}
print('size' in myCat)

# get() method in dict search for the passed key and prints the Value
# if the key is not present we can specify what to return instead of throwing error
# but do nat add the key to dict

print(myCat.get('size', 0))
print(myCat.get('voice', None))

print("------------------------")
# opposite to get() is setdefault(), this adds the key specified to dict
# and the value can't be change using this method

print(myCat.setdefault('size', 'Skinny'))
print(myCat.setdefault('age', 3))
print(myCat)
