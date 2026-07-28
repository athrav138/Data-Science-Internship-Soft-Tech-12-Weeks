class Rectangle:
    
    def __init__(self,l,b):
        self.length = l
        self.breadth = b
        
    def cal_area(self):
        self.area = self.length * self.breadth
        
    def display(self):
        print("The area of Rectangle is: ",self.area," sq.unit")
        
r1 = Rectangle(10,20)
r1.cal_area()
r1.display()
