
class Myclass:
    #public var(instance)
    public_var="I am public"
    Balance=0
    #private variable(cannot be accessed outside the class)
    __private_var="I am private "
    __password_var="1234 "
    #protected variable
    _protected_var= " I am protected"



object=Myclass()
print(object.public_var)
print(object._protected_var)
print(object.Balance)
# print(object.__private_var)
# print(object.__password_var)