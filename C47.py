import random

random.seed(124)

for i in range(10):
    print(random.randrange(1, 11, 2), end=", ")
print()
for i in range(10):
    print(random.randint(0, 10), end=", ")
