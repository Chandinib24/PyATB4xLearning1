#Method overiding
#child or subclass can have same name method as the parent or super class

class Shape:
    def area(self):
        print("Area of the shape")

class Rectangle(Shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width

    def area(self):
        return self.length*self.width

class Circle(Shape): # we can overide the methods of our parents
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return 3.14*self.radius*self.radius

Shape1=Rectangle(3,4)
print(Shape1.area())

Shape2=Circle(10)
print(Shape2.area())