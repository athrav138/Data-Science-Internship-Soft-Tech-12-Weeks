class Person:
    def getdata(self, n, a):
        self.name = n
        self.age = a

    def display(self):
        print("Name is:", self.name)
        print("Age is:", self.age)

class Student(Person):
    def getdata(self,n,a,per):
        super().getdata(n,a)
        self.per = per

    def display(self):
        super().display()
        print("Percentage is:", self.per)

class Designation:
    def getdata(self,desig):
        self.desig = desig

    def display(self):
        print("Designation is: ",self.desig)

class Employee(Student,Designation):
    def getdata(self,n,a,p,sal,des):
        Student.getdata(self,n,a,p)
        Designation.getdata(self,des)
        self.sal = sal

    def display(self):
        Student.display(self)
        Designation.display(self)
        print("Salary is: ",self.sal)

e1 = Employee()
e1.getdata("Atharv",17,94,19212818281,"Tester")
e1.display()