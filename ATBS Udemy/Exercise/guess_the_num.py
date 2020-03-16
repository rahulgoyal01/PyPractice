# this is guess the number game
import random

def guess():

    random_no = random.randint(1,50)
    count = 0
    while count < 6:
        count = count + 1
        num = int(input())
        if num < random_no:
            print("Your guess is too low.")
        elif num > random_no:
            print("Your guess is too high.")
        else:
            break

    if num == random_no:
        print("Hooray! You got my number in %d tries." % count)
    else:
        print("You are out of tries, the number I was thinking of is %d" % random_no)
    return

try:
    print("Hello. What is your name?")
    name = input()
    print('Well, %s, I am thinking of a number betwwen 1 and 20.\nTake a guess' % name)

    guess()
except:
    print("Unknown Error")
