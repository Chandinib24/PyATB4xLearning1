

# *args->multiple argument with no limits
#the below function is the no retun type with arguments
def print_argumets(*args):
    print(args[0])

print_argumets("Chandini","savitha","basavaraju",10,20)
print_argumets("amit","Ram")
print_argumets("Ram",10)
print_argumets("10","Ram")
print_argumets()# minimum 1 argument is important

print("amit")
print("Pramod","amit")
# print can take any number of arguments