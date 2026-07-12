class Display:
  def display(self):
    print("Hello")

class Display2(Display):
  def display(self):
    print("Hello WOrkd")

d2 = Display()
d2.display()

d1 = Display2()
d1.display()
