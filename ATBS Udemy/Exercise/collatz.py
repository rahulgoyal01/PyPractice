def collatz(number):

    if number % 2 == 0 :
        print(number // 2)
        return number // 2
    else:
        print(3 * number + 1)
        return 3 * number + 1

try:
    num = int(input("Please enter a value: "))
    while num != 1:
        num = collatz(num)
except:
    print("Kidnly provide only integer values.")
