# Class and Object Assignment
#
#
# Create a Employee Class
# A - name,age, phone, address, eid
# B - walk, talk, printdetails,
# with the Constructor which will set the values
# Ask the user about the information for E1, E2
# print the details of the E1, E2 via the print employee functions.

class Employee():
    ename=None
    eage=None
    ephone=None
    eaddr=None
    eemaid=None

    def ___init__(self,ename,eage,ephone,eaddr,eemaid):
        self.ename=ename
        self.eage=eage
        self.ephone=ephone
        self.eaddr=eaddr
        self.eemaid=eemaid

    def walk(self):
        print("Employee is waking\n",self.ename,self.eage,self.ephone.self.eaddr,self.eemaid)


    def talk(self):
        print("Employee is talking\n", self.ename, self.eage, self.ephone.self.eaddr, self.eemaid)


e1name = input("Enter the employee name\n")
e1age = input("Enter the employee age\n")
e1phone= input("Enter the employee phone number\n")
e1address = input("Enter the employee address\n")
e1id = input("Enter the employee eid\n")

e2name = input("Enter the employee name\n")
e2age = input("Enter the employee age\n")
e2phone= input("Enter the employee phone number\n")
e2addresss = input("Enter the employee address\n")
e2id = input("Enter the employee eid\n")

employee1=Employee(e1name ,e1age,e1phone,e1address,e1id)
print(employee1)
employee1.walk()
employee1.talk()

employee2=Employee(e2name ,e2age,e2phone,e2address,e2id)
print(employee1)
employee2.walk()
employee2.talk()










