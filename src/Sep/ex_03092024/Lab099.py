#Take the input and crate the class in function

class Person:
      def __init__(self):
          self.name=input("Enter your name \n") # it is a default constructor no arguments
          self.age=input("Enter your age \n")
          self.phone=input("Enter your phone \n")
          self.occupation=input("Enter your occupation \n")

      def name_of_the_function_to_display(self):
          print(f"Name is {self.name}")
          print(f"age is {self.age}")
          print(f"phone is {self.phone}")
          print(f"occupation is {self.occupation}")


#create an object
Person1=Person()
#call the display function
Person1.name_of_the_function_to_display()