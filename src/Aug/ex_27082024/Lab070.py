#function scope

global_b=12
def my_function():
    a=10 #local variable within function
    print(a)
    print(global_b)

def f1():
    print(global_b)
my_function()
print(global_b)