class Person:
    def getdata(self, n, a):
        self.name = n
        self.age = a

    def display(self):
        print("Name is:", self.name)
        print("Age is:", self.age)

class Student():
    def getdata(self,per):
        self.per = per

    def display(self):
        print("Percentage is:", self.per)


class Employee(Person,Student):
    def getdata(self,n,a,p,sal):
        Person.getdata(self,n,a)
        Student.getdata(self,p)
        self.sal = sal

    def display(self):
        Person.display(self)
        Student.display(self)
        print("Salary is: ",self.sal)

e1 = Employee()
e1.getdata("Atharv",17,94,19212818281)
e1.display()