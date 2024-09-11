#Inheritance
#single Inheritance

class Father():
    key="2BHK"

    def car(self):
        print("Fathe car!!!","ALTO",self.key)

class son(Father): #created the son class where father class is  inherited
       key2="3BHK"

       def Home(self):
           print("3BHK")

       def truck(self):
           print("He has truck")


father_obj=Father()
father_obj.car()

son_obj=son()
son_obj.car()

