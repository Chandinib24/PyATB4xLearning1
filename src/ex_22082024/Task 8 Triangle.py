"""
Task 8 - Triangle classifier
Write a program that classifies a triangle based on its side lengths.

Given three input values representing the lengths of the sides,

determine if the triangle is equilateral (all sides are equal),

isosceles (exactly two sides are equal), or scalene (no sides are equal).

Use an if-else statement to classify the triangle.
"""

side1=input("Enter the length of side1: \n")
side2=input("Enter the length of side2: \n")
side3=input("Enter the length of side3: \n")
if(side1==side2 and side1==side3):
    print("The triangle is equilateral")
    # elif (n1 == n2 and n1 != n3) or (n2 == n3 and n2 != n1) or (n1 == n3 and n1 != n2):
elif side1==side3 or side2==side1:
    print("The triangle is isosceles")
else:
    print("scalene")

