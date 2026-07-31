#student Roaster

class Student:
    total_student=0
    def __init__(self,name,grade):
        self.name=name
        self.grade=grade
        Student.total_student+=1
s1=Student("Rahul","A")
s2=Student("Anu","B")
s3=Student("Akshay","A")
print("Total Student=",Student.total_student)