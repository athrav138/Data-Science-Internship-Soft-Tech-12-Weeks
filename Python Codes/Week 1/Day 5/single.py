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

s1 = Student()
s1.getdata("shree", 18, 75)
s1.display()