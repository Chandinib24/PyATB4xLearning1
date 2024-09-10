class calc:
    def __init__(self,a,b):
     self.a=a  #parameterized constructor
     self.b=b #parameterized constructor


    def sum(self, a,b):
      return self.a+self.b

    def sub(self, a,b):
      return self.a-self.b

    def mul(self, a,b):
      return self.a*self.b

    def div(self, a, b):
        return self.a/self.b

obj_ref=calc(30,15)
output=obj_ref.sum()
output2=obj_ref.sub()
print(output)
print(output2)


