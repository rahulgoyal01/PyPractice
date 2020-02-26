import random
# Random module helps in selecting a random item from a set
# of data.
# random.choice(population, k) where first argument is
# dataset and k is size
# random.sample(population, k) where first argument is
# dataset and k is size. here k cannot be greater than
# size of dataset
list = [20, 30, 40, 50 ,60, 70, 80]
sampling = random.sample(list, k=5)
print(sampling)

list = [20, 30, 40, 50 ,60, 70, 80]
choice = random.choices(list, k=10)
print(choice)
