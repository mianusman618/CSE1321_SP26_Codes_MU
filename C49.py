import time

print("10 seconds countdown started...")
print("Loading")
for x in range(10, 0, -1):
    print("*",end="")
    time.sleep(2)
