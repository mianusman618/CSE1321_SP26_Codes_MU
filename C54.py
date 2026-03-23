from C53 import random_num, myabs
import random
import time

num1=random_num(time.time())
print("Our Random Num = ",num1)

num2=random.randint(0,100)
print("Random Library num = ",num2)

print(myabs(15))