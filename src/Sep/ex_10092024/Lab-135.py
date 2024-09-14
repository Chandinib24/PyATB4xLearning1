#try,except and Finally
try:
    num1=int(input("Enter a number\n"))
    num2=int(input("Enter a number\n"))
    result=num1/num2
except ValueError as ve:
    print("Value error, you have entered a string instead of int ")
except ZeroDivisionError as zde:
    print("Dont use num2 as Zero")
else:
    print(f"Result is",{result})

finally:
  print("This code will always be executed")
