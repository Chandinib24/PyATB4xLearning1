#User defined fumctions
# 1. They cant return anything--> No return
# 2. They can return something
# They have parameters
# They dont have parameters

#  1. They cant return anything--> No return
#No return type no parameter/arguments NRNP

def greet():
    print("Hello world")

result=greet()
print(result)

#2.No return type  and with argument
def greet_by_name(name):
    print("Hello", name)
greet_by_name("Pramod")

#3.No return type  and with default argument

def say_hello_default_arg(name="Pramod"):
    print("Hello",name)
say_hello_default_arg() # if we do not pass any alue then it will return defuat value  i.e pramod
say_hello_default_arg("Sachin")
say_hello_default_arg(name="chandu") #positional argument


def multiple_args(name1="Chandini",name2="Vasrhini",name3="Bhoomika"):
    print("Multiple Arguments", name1,name2,name3)
multiple_args("Ram","Sita","Krishna")

#4.Argument+Return type
def sum_of_two_numbers(num1,num2):
    return num1+num2
result=sum_of_two_numbers(10,32)
result=sum_of_two_numbers(num1=10,num2=32) #positional
print(result)
def sum_of_two_numbers_by_default(num1=100,num2=400):
    return num1+num2
result=sum_of_two_numbers_by_default()
print(result)


