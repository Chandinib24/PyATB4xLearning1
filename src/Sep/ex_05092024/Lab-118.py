#Hybrid Inheritance

#Multiple types of inheritance
#such as single,
#multiple
#multi level inheritance

class A:
    def MethodA(self):
        return "MethodA"

class B(A):
    def MethodB(self):
        return "MethodB"
class C(A):
    def MethodC(self):
        return "MethodC"

class D(B,C):
    def MethodD(self):
        return "MethodD"
d=D()
print(d.MethodC())
print(d.MethodA())
print(d.MethodB())
print(d.MethodD())