# Method Overloading

class Arithmetic:
  @staticmethod
  def add(a=0,b=0,c=0):
    print("Addition: ",(a+b+c))

  def multi(self,a=1,b=1,c=1):
    print("multiplication: ",a*b*c)

Arithmetic.add(10)
Arithmetic.add(10,20)
Arithmetic.add(10,20,30)

a1 = Arithmetic()
a1.multi(10)
a1.multi(10,20)
a1.multi(10,20,30)




