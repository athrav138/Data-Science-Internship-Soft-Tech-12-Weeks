class Person:
    def __init__(self, n, a):
        self.name = n
        self.age = a

    def display(self):
        print("Name is:", self.name)
        print("Age is:", self.age)

s1 = Person("shree", 18)
s1.display()