#Encapsulation
#Hide data members(class variables,instances variables)
#By using only the methods

class Car:
    model=None
    name=None
    password=123

    def __init__(self):
        self.password="Chandini"

    def change_password(self):
        print(self.password)

obj_ref=Car()
print(obj_ref.change_password())