
class Person:
    #Attributes
    id=None
    name=None
    phone_no=None
    Gender=None
    height=None
    address=None

    #Behaviour
    def talk(self):#NRNA #self will be the first argument in every behaviour
        print("I can talk")

    def sleep(self,name): #Arg with No return
        print("I am a method!")
        print("sleep",name)

    def sleep2(self, name):  # Arg with return
            print("I am a method!")
            return None

    def walk(self):  # NRNA #self will be the first argument in every behaviour
        print("I can walk")

    def walk_return(self): #No argument with return
        return "I am walking"


#create an object of the class
#ojectRef=ClassName()-->object
chandini=Person()
chandini.name="chandini"
print(chandini.name)
chandini.talk()