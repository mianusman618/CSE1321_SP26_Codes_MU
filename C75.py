# s1=25
# s2=23
# s3=27
# s4=22
# s5=29
student_list=[]
user_input=int(input("Enter Number of Students ="))
for i in range(user_input):
    print("Enter age of Student ",i)
    user_input2=float(input())
    student_list.append(user_input2)

sum=0
for i in range(len(student_list)):
    sum+=student_list[i]
print("Avg Age = ",sum/len(student_list))