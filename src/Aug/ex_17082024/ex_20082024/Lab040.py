# Problem to find the max between 3 numbers

# lOgic building
# 1.user inputs--num1,num2,num3 --integerss
# 2.o/p-->integer or string with max number

# Logic? if else-->for 1 condition
# more 1 condition--> if elif else

# syntax

# if condition 1:
# print("Do 1")
# elif condition 2:
# print("Do 2")
# elif condition 3:
# print("Do 3")
# else:
# print ("Do 4")

num1 = int(input("Enter the num1 \n")),  # 5  , #10
num2 = int(input("Enter the num2 \n")),  # 3   ,#12
num3 = int(input("Enter the num3 \n")),  # 2   ,#11

# 5>2 and 5>2-->true-> 5
# num1>num3 and num1>num2 -->num 1

# 12>11 and 12>10 -->true->12
# num2>num3 and num2>num1 -->num 2

if num1 > num3 and num1 > num2:
    print("Max is", num1)
elif num2 > num3 and num2 > num1:
    print("Max is", num2)

else:
    print("Max is", num3)

    result = max(num1, num2, num3)
    print(result)
