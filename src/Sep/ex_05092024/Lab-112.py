#Single inheritance
class Parent:
    Gold="2kg"


    def BHK2(self):
        print("2BHK")

class child(Parent):
    def BHK3(self):
       print("3BHK")

child_obj=child()
print(child_obj.Gold)
#child_obj.BHK3()#'Parent' object has no attribute 'BHK3'
child_obj.BHK2()

Father_obj_ref=Parent()
Father_obj_ref.BHK2()
Father_obj_ref.BHK3()
