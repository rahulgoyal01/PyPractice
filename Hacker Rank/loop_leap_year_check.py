
def it_leap(year):
    leap = False

    if (year % 4 == 0) & (year % 100 != 0):
        leap = True
    elif (year % 400 == 0):
        leap = True
    elif (year % 100 == 0):
        leap = False
    else:
        leap = False
    return leap

year = int(input())
print(it_leap(year))
