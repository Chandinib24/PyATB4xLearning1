#Exceptions
print("---start of the program")
try:
   a=int(input("Ent a num1"))
   b=int(input("Ent a num2"))
   c=a/b #ZeroDivisionError: division by zero  and ValueError: invalid literal for int() with base 10: 'sjh'
   print("Result Div is", c)
except Exception as e:#exception is a class containg multiple classes
    print(e)
    print("Please check your inputs,  it should not be string or Zero")


print("---end of the program")