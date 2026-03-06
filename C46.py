import random
#random.seed(12)
for i in range(10):
    print(random.randrange(1, 1100, 2), end=", ")
print()
for i in range(10):
    print(random.randint(0, 1100), end=", ")
