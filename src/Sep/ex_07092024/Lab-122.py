#OOPS
#Class-Blueprint
#object-instance of a class
#encapsuation-private,pubic,protected
#Inheritance-single,multilevel,multiple,heirarchy,hybrid
#Polymorphism-method overriding
#self,super,__init(constructor)

#Abstraction
#Hide the details and show what is required

from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self,name):
        self.name=name

    @abstractmethod # incomplete in nature so some method has to complete this
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print("Bark")

anm_obj=Dog("pp")
anm_obj.sound()

