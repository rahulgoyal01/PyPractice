class Square:

    def __init__(self, sides):    # special method __init__
        self.sides = sides

square = Square(8)
print(square.sides)

class Car:
    def __init__(self, color):
        self.color = color

car = Car("blue")    # Note: you should not pass self parameter explicitly, only color parameter

print(car.color)
