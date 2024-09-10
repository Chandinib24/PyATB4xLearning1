class Dog: #class name always starts with captital
    #A
    name=None
    Breed=None
    color=None

    #B
    def sleep(self):
       print("Dog is sleping")

    def Bark(self):
       print("Dog is Barking")

dog1=Dog()
print(dog1.name)
dog1.name="Mow"
print(dog1.name)
dog1.sleep()

print("-------------------")
dog2=Dog()
print(dog1.name)
dog1.name="Chow"
print(dog1.name)
dog1.Bark()