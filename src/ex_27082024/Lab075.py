#Decorator

# two parts
# 1,Wrapper
# 2. call

def add_extra_security(func):
    def wrapper():
        print("1.berore the functio is called")
        print("2.Add helmet,dashcash,knee guards")
        func()
        print("3.After the fucntion is called")
        print("Secure driving")

    return wrapper()

# @ add_extra_security # it is decorator where it goes back to the top where func() is called and executes the code
# def driving_bike():
#     print("i am driving a bike")


@ add_extra_security # it is decorator where it goes back to the top where func() is called and executes the code
def driving_scooty():
    print("i am driving a scooty")

