#conditions and loops

#write a program to take user age and to find let him got o club or not

#Logic building'
# 1.user input -->data type-->integer
#output will be string-->user if he can go or not

# 2.Rough logic
#age<21-->user can't go
#age>21-->user can go

# 3.write the logic

age=input("Enter your age \n")
age=int(age)

if age<21:
    print(f"User can't go-->{age}")
else:
    print(f"User can go-->{age}")