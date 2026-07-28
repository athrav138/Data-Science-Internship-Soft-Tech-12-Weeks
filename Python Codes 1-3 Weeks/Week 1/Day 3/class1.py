class Student:

  def __init__(self,n,r):
    self.name = n
    self.roll = r

  def display(self):
    print("Display in parent")

class Marks(Student):
  
  def __init__(self,n,r,per):
    self.per = per
    super().__init__(n,r)

  def display(self):
    print("Name= ",self.name)
    print("Roll=",self.roll)
    print("Percentage=",self.per)

m1 = Marks("Shree","57",94.82)
m1.display()

s1 = Student("shree",83)
s1.display()