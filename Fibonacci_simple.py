
n = input("No. of terms to be shown in the Fibonacci Series:")
n = int(n)
print('Below are the Fibonacci series upto %d terms.' % n)
def fibonacci(number):

    result = []
    i = 0
    temp = 0
    first = 0
    scnd = 1

    while i < int(number):
        result.append(first)
        temp  = scnd
        scnd  = scnd + first
        first = temp
        i += 1
    return result

print(fibonacci(n))
