class Person:
    #class variables
    #instance variables
    # name="Amit" #Hardcoded value

    def __init__(self,name):
        self.name=name #constryctor is used to chage the value of instance variable during object creation

    def walk(self,name):
        print(self.name)

Amit=Person("Amit")
Pramod=Person("Pramod")
print(Amit.name)
print(Pramod.name)