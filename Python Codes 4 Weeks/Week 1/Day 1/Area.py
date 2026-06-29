import math

def rectangle_area(l,b):
  area= l*b 
  print("Area of Rectangle= ",area)

def circle_area(r):
  area = math.pi * r * r
  print("Area of Circle= ",area)

def triangle_area(h,b):
  area = 0.5 * h * b
  print("Area of traingle: ",area)


triangle_area(12,2)
circle_area(5)
rectangle_area(5,10)
