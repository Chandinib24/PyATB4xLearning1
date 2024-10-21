#create a program to sum of three numbers form user input

num1=int(input("Enter the number 1 \n"))
num2=int(input("Enter the number 2 \n"))
num3=int(input("Enter the number 3 \n"))

def sum_of_three_numbers(n1,n2,n3):
    return n1+n2+n3

result=sum_of_three_numbers(num1,num2,num3)
print(result)
result=sum_of_three_numbers(n1=num1,n2=num2,n3=num3)
print(result)

# if it does not return any value then o/p will be none
num1=int(input("Enter the number 1 \n"))
num2=int(input("Enter the number 2 \n"))
num3=int(input("Enter the number 3 \n"))

def sum_of_three_numbers(n1,n2,n3):
    print(n1+n2+n3)

result=sum_of_three_numbers(num1,num2,num3)
print(result)
result=sum_of_three_numbers(n1=num1,n2=num2,n3=num3)
print(result)

