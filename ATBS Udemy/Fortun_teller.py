import random

class Fortune:
    random_no=random.randint(1, 9)
    # check how to use these variables from init.
    def  __init__(self, name, color, age):
        self.name = name
        self.color = color
        self.age = age

    @classmethod
    def from_input(cls):
        return cls(
            input('Name: '),
            input('Color: '),
            int(input('Age: ')),
        )

    def random_fortune():
        random_no = random.randint(1, 9)
        if random_no == 1:
            print("you are in luck today")
        else:
            print("Bad Luck mate")


user = Fortune.from_input()
Fortune.random_fortune()
