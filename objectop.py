class Student:
    "information about the class"
    studentcount= 0
    def getdata(self,roll,name,course):
        self.roll=roll
        self.name=name
        self.course=course
        Student.studentcount=Student.studentcount+1
    def displaycount():
        print("num of student objects",Student.studentcount)
    def display(self):
        print("RollNo=",self.roll)
        print("name=",self.name)
        print("course=",self.course)
    def _del_(self):
        class_name=self._class_._name_
        print(class_name,"destroyed")
s1=Student()
s2=Student()
s3=Student()
s4=Student()
s1.getdata(102,"Anju","MCA")
s2.getdata(106,"Ansiya","MCA")
s3.getdata(115,"Dwany","MCA")
s4.getdata(129,"Raichel","MCA")
print(getattr(s1,"name"))
s1.display()
print("________")
s2.display()
print("________")
s3.display()
print("________")
s4.display()
Student.displaycount()
del s1

              

              

              
