#Overloading
#python does not support the method overloading
#in traditional sense

class MathUtils(object): #is a object -single inheritance
    #method overloading is not supported
  def add(self ,a,b):
      return a+b

  def add(self,a,b,c=10): # accepts only when default value is given 
      return a+b+c

math=MathUtils()
op1=math.add(2,3)
print(op1)