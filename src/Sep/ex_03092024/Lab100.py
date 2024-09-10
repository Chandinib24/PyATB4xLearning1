class calc:
    def __init__(self):
     print("DC") #non parameterized constructer


    def sum(self, a,b):
      return a+b

    def sub(self, a,b):
      return a-b

    def mul(self, a,b):
      return a*b

    def div(self, a, b):
        return a/b

obj_ref=calc()
a=int(input("Enter the value of a "))
b=int(input("Enter the value of b "))
object_sum=obj_ref.sum(2,3)
object_sub=obj_ref.sub(20,15)
object_mul=obj_ref.mul(20,30)
object_Div=obj_ref.div(30,15)

print(object_sum,object_sub,object_mul,object_Div)

