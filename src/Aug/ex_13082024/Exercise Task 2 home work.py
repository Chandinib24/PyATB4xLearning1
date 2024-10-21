""""
Create a program , take 2 inputs from the user num1, num2 and give them
max
pow num1 to num2
sub, mul, sum, div.
Format your out with f{""}

"""

num1 =int(input("Enter the num1: "))
num2 =int(input("Enter the num2: "))

print(num1)
print(num2)

print("The power of num1 to num2 is" ,pow(num1,num2))
print("The sum of num1 and num2 is", int(num1+num2))
print("The subtraction of num1 from num2 is", int(num1-num2))
print("The div of num and num2 is", int(num1/num2))

print("Formated_num1 is : ", f"{num1 : .5f}")
print("Formated_num2 is : ", f"{num2 : .5f}")
