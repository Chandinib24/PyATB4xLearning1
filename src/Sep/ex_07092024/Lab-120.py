#Method overriding-same name in parent and child
#child always overide the parent fuction
#super means call my parent fucntion
class Grandfather():
    x=12
    def home(self):
        print("Old home")

class Father(Grandfather):
    a=10
    def home(self):
        print("1BHK")
        print(self.a)
        print(super().x)

class Son(Father):
    b=10
    def home(self):
        super().home()#Father behaviour by super
        print(super().a)#Father attributes by Super
        print("No home")
        print(self.b)
        print(super().x)

Pramod=Son()
Pramod.home()
print(Pramod.x)