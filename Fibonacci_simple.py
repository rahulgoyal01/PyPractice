number = input("No. of terms to be shown in the Fibonacci Series:")
result= []
i = 0
temp = 0
first = 0
scnd = 1

while i < int(number):
    print(first)
    temp = scnd
    first = temp
    scnd = scnd + first
    i += 1
