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
        return self(name,color,age)

    @staticmethod
    def random_fortune():
        random_no = random.randint(1, 9)
        if random_no == 1:
            print("you are in luck today")
        else:
            print("Bad Luck mate")


    def greeting(self, name):
        return "Hi" + name


user = Fortune.from_input()
Fortune.greeting("Rahul")
Fortune.random_fortune()
