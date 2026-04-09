def regular_function(self):
    print("inside regular function")

class Student:
    name=""
    id=""
    dob=""
    Major=""
    CGPA=0
    courses=[]
    def register_course(self,P2,P3=0):
        print("inside register course")
    def another_function(self):
        print("inside another function")
        print("This is ",self.name)

if __name__=="__main__":
    s1=Student()
    s2=Student()
    s1.name="Alice"
    s2.name="bob"
    s1.Major="CS"
    s2.Major="SE"
    print(s1.name)
    s1.another_function()
    s2.another_function()