import random
class Fortune:
    name = ""
    color = ""
    age = 0

    def  __init__(self, name, color, age):
        self.name = name
        self.color = color
        self.age = age

    @staticmethod
    def from_input(self):
        name = input('Name: ')
        color = input('Color: ')
        age = int(input('Age: '))
        return Fortune(name,color,age)

    @classmethod
    def random_fortune(self):
        print("Hi " + self.name)
        random_no = random.randint(1, 9)
        if random_no == 1:
            print("you are in luck today")
        else:
            print("Bad Luck mate")


user = Fortune.from_input()
user.random_fortune()
