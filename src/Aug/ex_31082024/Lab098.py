
class Employee:
    Name=None
    age=None
    Phoneno=None
    address=None
    eid=None

    def __init__(self, name, age,Phoneno,address,eid):
        print("constructer is called")
        self.name=name
        self.age=age
        self.Phoneno=Phoneno
        self.address=address
        self.eid=eid

    def empData(self):
        print("Employee Name:", self.name)
        print("Employee Age:", self.age)
        print("Employee Phone number:", self.phoneno)
        print("Employee Address:", self.address)
        print("Employee Eid:", self.eid)

    E1 = empData(input("Enter name of employee"), input("Enter age of employee"),
                  input("Enter Phone number of employee"), input("Enter address of employee"),
                  input("Enter Eid of employee"))
    E2 = empData(input("Enter name of employee"), input("Enter age of employee"),
                  input("Enter Phone number of employee"), input("Enter address of employee"),
                  input("Enter Eid of employee"))

    E1.empData()
    E2.empData()
