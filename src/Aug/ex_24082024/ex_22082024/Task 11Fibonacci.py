#Fibonaci series 0,0+1, 0+1+1, n = 7 0, 1, 2, 3, 5, 8, 13

num=int(input("Enter a number to create Fibonacci series : \n"))
series=[]
a,b=0,1
for i in range(num+1):
    series.append(a)
    a, b = b, a + b

print(f"Fibonacci series for number {num} is {series}")