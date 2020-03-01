#Self explanation

# It's time to explain the self parameter used in previous tasks.
# The self parameter is a Python convention. self is the first parameter
# passed to any class method. Python will use the self parameter to refer
# to the object being created. Implement the add method. It should add amount to the current field.

class Complex:
    def create(self, real_part, imag_part):
        self.r = real_part
        self.i = imag_part

class Calculator:
    current = 0

    def add(self, amount):
        self.current += amount

    def get_current(self):
        return self.current

value = Calculator()
value.add(5)
