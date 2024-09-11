#static methods
#static methods is a method that belongs to
#class rather than instance of the class

class Mathoperations():
    def Div(self,a,b):
        return a/b
    def mul(self,a,b):
        return a*b
    @staticmethod
    def Sum(a,b):
        return a+b

#non static methods object creation is mandatory
object_ref=Mathoperations()
output=object_ref.Div(10,5)
output=object_ref.mul(10,5)


print(output)
#static methods can be called directly without creating a object, static belogs to class so no self is used
print(Mathoperations.Sum(5,9))