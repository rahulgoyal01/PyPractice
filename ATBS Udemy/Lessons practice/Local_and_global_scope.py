#
#

eggs = 101 # this is a global variable

def spam():
    eggs = 99 #Local to function Spam
    bacon()
    print(str(eggs) + " eggs are from local spam")


def bacon():
    ham = 101
    eggs = 0    #Local to function bacon
    print(str(eggs) + " eggs are from local bacon")
    return       # return None value

print(str(eggs) + " eggs are from global")
spam()
