class A:

    def method(self):
        return "MethodA"
class B:
    def method(self):
        return "MethodB"

class C(B,A):
    pass

c=C()
print(c.method())