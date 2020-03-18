# https://www.geeksforgeeks.org/python-map-function/


def listToStr(list):
    #long way without any methods
    str1 = ''
    for i in range(len(list)):
        if list[i] != list[-2] and list[i] != list[-1]:
            str1 = str1 + str(list[i]) + ', '
        elif list[i] == list[-2]:
            str1 = str1 + str(list[i])
        else:
            str1 += ' and ' + str(list[i])

    return str1





spam = ['apples', 'bananas', 'tofu', 'cats']

print(listToStr(spam))

#short ways using Join and Map methods
string1 = ', '.join(map(str, spam[:-1])) + ' and ' + str(spam[-1])
string2 = ', '.join([str(elem) for elem in spam])

print(range(len(spam)-2))
print(string1)
print(string2)
