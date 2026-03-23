# s1=25
# s2=23
# s3=27
# s4=22
# s5=29
student_list=[25,23,27,22,29]
sum=0
for i in range(len(student_list)):
    sum+=student_list[i]
print("Avg Age = ",sum/len(student_list))