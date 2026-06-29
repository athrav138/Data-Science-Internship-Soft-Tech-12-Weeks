class Person:
    def __init__(self, n, a):
        self.name = n
        self.age = a

    def display(self):
        print("Name is:", self.name)
        print("Age is:", self.age)

class Student(Person):
    def __init__(self, n, a, per):
        super().__init__(n, a)
        self.per = per

    def display(self):
        super().display()
        print("Percentage is:", self.per)

s1 = Student("shree", 18, 75)
s1.display()