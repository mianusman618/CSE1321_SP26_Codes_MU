myList1=[]
myList2=["Abc",50,27,12,45,10.6]
print(len(myList2))
print("My List 2 = ",myList2)
myList2.append(100)
print("My List 2 = ",myList2)
myList2.append("XYZ")
print("My List 2 = ",myList2)
myList2.insert(0,555)
print("My List 2 = ",myList2)
myList2.insert(4,200)
print("My List 2 = ",myList2)
myList2[1]="def"
print("My List 2 = ",myList2)

bool_var=27 not in myList2
print("Bool var ",bool_var)
