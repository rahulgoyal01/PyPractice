def collatz(number):

    if number % 2 == 0 :
        result = number // 2
    else:
        result = 3 * number + 1

    print(result)
    while result != 1:
        collatz(result)
        return

try:
    num = int(input("Please enter a value: "))
    num = collatz(num)
except:
    print("Kidnly provide only integer values.")
