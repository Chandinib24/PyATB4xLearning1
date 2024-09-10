a=10

class Person:
    b=11 #instance variable belogs to class

    def print_info(self):
        global a #Declare it as global
        a="Hello"
        print(a)
        print(self.b)

object_ref=Person()
object_ref.print_info()