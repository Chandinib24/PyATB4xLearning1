#def sum_of three numbers a,b,c
#retun a+b+c

# def sum_of_three_num(a,b,c):
#     return a+b+c

nnn=lambda a,b,c:a+b+c
print(nnn(31,26,27))

def find_even_odd(num):
    if num%2==0:
        print("even")
    else:
        print("odd")
#find_even_odd(6)

check_even_odd=lambda num: "Even" if num%2==0 else "odd"
print(check_even_odd(15))