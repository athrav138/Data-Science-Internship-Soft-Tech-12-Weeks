class Person:
    def getdata(self, n, a):
        self.name = n
        self.age = a

    def display(self):
        print("Name is:", self.name)
        print("Age is:", self.age)

class Student(Person):
    def getdata(self, n, a, per):
        super().getdata(n, a)
        self.per = per

    def display(self):
        super().display()
        print("Percentage is:", self.per)


class Employee(Student):
    def getdata(self,n,a,p,sal):
        super().getdata(n,a,p)
        self.sal = sal

    def display(self):
        super().display()
        print("Salary is: ",self.sal)

e1 = Employee()
e1.getdata("Atharv",17,94,19212818281)
e1.display()