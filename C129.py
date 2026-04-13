class student:

    def __init__(self):
        self.name = ""
        self.GPA = 0.0
        self.courses_list = []
    def print_info(self):
        print("Name = ",s1.name)

if __name__=="__main__":
    s1=student()
    #s1.courses_list=[]
    s2=student()
    #s2.courses_list=[]

    s1.name="Alice"
    s2.name="Bob"

    s1.courses_list.append("CSE-1321")
    s2.courses_list.append("XYZ")

    print(s1.name," is taking ",s1.courses_list)
    print(s2.name, " is taking ", s2.courses_list)