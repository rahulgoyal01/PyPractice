import random

class Fortune:

    # check how to use these variables from init
    def  __init__(self, name, color, age):
        self.name = name
        self.color = color
        self.age = age

    @classmethod
    def from_input(self):
        name = input('Name: ')
        color = input('Color: ')
        age = int(input('Age: '))
        return self(name, color, age)

    def random_fortune(self):
        random_no = random.randint(1, 9)
        print("Hi " +  self.name)
        if random_no == 1:
            print("you are in luck today")
        else:
            print("Bad Luck mate")


#    def greeting(name):
#        return "Hi" + name

user = Fortune.from_input()
#print(Fortune.greeting(" Rahul"))
user.random_fortune()
