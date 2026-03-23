user_input=input("Enter Comma Sep Values = ")
print(user_input)

myList=user_input.split(",")
print(myList)
for i in range(len(myList)):
    myList[i]=int(myList[i])
print(myList)
sum=0
for i in range(len(myList)):
    sum+=myList[i]
print(sum)