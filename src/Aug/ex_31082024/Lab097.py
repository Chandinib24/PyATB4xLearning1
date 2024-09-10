#concstructor
#special function in clas ---init()---
#It will be automatically called when you craete an object

class Dog:
    name=None
    age=65

    def __init__(self,name,age):
       print("called,object is created")
       self.name=name
       self.age=age

    def sleep(self):
        print("sleeping")
        print("Who is sleeping", self.name)

dog1=Dog("chow",10)
print(dog1.name)
print(dog1.age)
dog1.sleep()

dog2=Dog("mow",15)
print(dog2.name)
print(dog2.age)
dog2.sleep()