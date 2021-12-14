class Employee:
    def __init__(self,name,emid,salary):
        self.name=name
        self.emid=emid
        self.salary=salary
list=[]
n=int(input("enter employees"))
for i in range (0,n):
    name=input("enter your name")
    emid=int(input("enter your id"))
    salary=int(input("enter your salary"))
    list.append(Employee(name,emid,salary))
for obj in list:
    print(obj.name,obj.emid,obj.salary)
