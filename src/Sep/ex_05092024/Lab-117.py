#Hierachical inheritance

class Father():
    def BHK1(self):
        print("1BHK")

class Pramod(Father):
    def BHK2(self):
        print("BHK2")

class Amit(Father):
    def BHK3(self):
        print("BHK3")

class Lucky(Father):
    def nohouse(self):
        print("no house")

pramod=Pramod()
pramod.BHK1()
pramod.BHK2()

amit=Amit()
amit.BHK1()
amit.BHK3()
#amit.BHK2()
