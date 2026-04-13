class Student:
	name = ""
class Classroom:
	list_of_students = [] # the danger

s1 = Student()
s1.name = "Alice"
s2 = Student()
s2.name = "Bob"

c1 = Classroom() # created a classroom
c2 = Classroom() # created another classroom

c1.list_of_students.append(s1) # added Alice to class 1
c2.list_of_students.append(s2) # added Bob to class 2

print(c1.list_of_students) # prints [‘Alice’, ‘Bob’] THIS IS A PROBLEM
print(c2.list_of_students) # prints [‘Alice’, ‘Bob’] BOTH CLASSROOMS ARE SHARING THE SAME STUDENTS