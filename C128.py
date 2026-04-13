class student:
    name=""
    courses_list=[]
if __name__=="__main__":
    s1=student()
    s2=student()
    s1.name="Alice"
    s2.name="Bob"
    s1.courses_list=[]
    s2.courses_list=[]

    s1.courses_list.append("CSE1321")
    s2.courses_list.append("XYZ")

    print(s1.name," is taking ",s1.courses_list)
    print(s2.name, " is taking ", s2.courses_list)
