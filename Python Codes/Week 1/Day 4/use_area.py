from area import circle_area
from area import rectangle_area as ra
import area 
from area import *

r = float(input("Enter radius of circle: "))
print("Area of circle is: ",circle_area(r))

l = float(input("Enter the length of rectangle: "))
b = float(input("Enter the breadth of rectangle: "))
print("The area of rectangle is: ",area.rectangle_area(l,b))

h = float(input("Enter the height of Traingle: "))
b = float(input("eneter the base of triangle: "))
print("the area of Triangle is: ",triangle_area(h,b))

s = float(input("Enter the side of sqaure: "))
print("The area of the square: ",square_area(s))