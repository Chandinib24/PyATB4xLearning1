#
# class Father():
#      key="ABC"
#       __password="Private"
#
#    def __show_password(self):
#     print(self.__password)
#    def fater_money(self):
#     return 5
#
#    def __show_everything(self):
#        self.__showpassword
#
#    def Home(self):
#        return "I have the home Father"
#
# class Mother():
#
#     def Mother_money(self):
#         return  2
#
#     def Home(self):
#         return "I have the home mother"
# #Diamond problem of multilevel inheritance is when two fuctions have same name like home then it will be confused
# # to which one to print so, we use multiple inheritance where it will print the function which is mentined first
# #class Son(Father,Mother):#MRO method resolution order
#     pass
# class Son2(Mother,Father):
#     pass
#
# s=Son()
# print(s.Mother_money())
# print(s.fater_money())
# print(s.Home())
#
# s2=Son2()
# print(s2.Home())
#
