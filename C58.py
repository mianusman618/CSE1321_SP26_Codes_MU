msg="Hello World"
print("Length of string = ",len(msg))
#Output: “dlroW olleH”
for i in range(len(msg)-1,-1,-1):
    print(msg[i],end="")