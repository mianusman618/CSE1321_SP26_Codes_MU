myList1=[]
myList2=["Abc",50,27,12,45,27,10.6,27]
print(len(myList2))
print("My List 2 = ",myList2)

del myList2[4]
print("My List 2 = ",myList2)

result=myList2.pop(0)
print("My List 2 = ",myList2)
print("result = ",result)

remove_result=myList2.remove(27)
print("My List 2 = ",myList2)
print("remove result = ",remove_result)

myList2.clear()
print("My List 2 = ",myList2)
