#- Write a Python program to calculate the area of a circle given its
# radius using the formula ``` area=π×r^2``` ( Take pie as 3.14)
import math

radius= int(input("Enter the radius of circle"))
print(radius)
pi=math.pi
area=math.pi*(radius**2)
print(f"area of the circle is,{area:.2f}")