#Take user input and calculate sum,mul,sub,div
#calc

num1=int(input("Enter the num1"))
num2=int(input("Enter the num2"))

print(type(num1))
print(type(num2))

#here num1 and num2 -any operation performed will be concatinated
#convert str--> to int by adding int

print("Sum is",num1+num2)
print("Subtraction is",num1-num2)
print("Mul is",num1+num2)
print("Div is",num1/num2) #though data type is int , there are high chances that float will come when we divide  #Python is very smart langugae - whenever we divide it always gives decimal