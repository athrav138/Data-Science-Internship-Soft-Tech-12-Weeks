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
    


class Employee(Person):
    def getdata(self,n,a,sal):
        super().getdata(n,a)
        self.sal = sal

    def display(self):
        Person.display(self)
        print("Salary is: ",self.sal)

e1 = Employee()
e1.getdata("Atharv",18,1898219)
e1.display()


s1 = Student()
s1.getdata("Shree",18,75)
s1.display()