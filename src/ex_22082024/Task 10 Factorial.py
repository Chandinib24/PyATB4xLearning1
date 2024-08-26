#Task #10 -
#Factorial n = 5 5! -->54321 -> 120 3! -> 321 -> 6 4! -> 432*1 -> 24

num=int(input("Enter a number for which you want factorial : \n"))
fact=1
for i in range(1,6):
    print(i)
    fact=fact*i
    i=i+1

print(f"Factorail of {num} is {fact} " )