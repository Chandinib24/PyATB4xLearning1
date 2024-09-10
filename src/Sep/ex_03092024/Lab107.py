#Web automation -selenium
#Page- you  are going to automate

class VWOloginpage:

    def __init__(self,email_arg,password_arg):
        self.email=email_arg
        self.password=password_arg

    def login_confirm(self):
        if self.email=="chandinib21@gmail.com"  and self.password =="Pass123":
            print("Allowed to login")

        else:
            print("Not allowed")
#This is the end of class

email=input("Enter the email \n")
password =input("Enter the password \n")

login_ref=VWOloginpage(email,password)
login_ref.login_confirm()


