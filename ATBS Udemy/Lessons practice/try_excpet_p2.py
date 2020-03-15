

def cats(num):
    try:
        if int(num) >= 4:
            print("These are lot of cats.")
        else:
            print("That is not that many cats.")
    except ZeroDivisionError: #print this if ZeroDivisionError
        print("Don't try naughty things.")
    except ValueError: #print this if value error
        print("This is not the correct the value. Please check again.")
    except: # print this if any other type of error
        print("You entered something else than a number.")


num = input("How many cats you have: ")
cats(num)
