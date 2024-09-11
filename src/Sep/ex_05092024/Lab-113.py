#Multilevel inheritance

class Grand_Father():
    gold=("2kg")

    def BHK1(self):
        print("BHK1")

class Father(Grand_Father):
    diamond="22karat"
    def bhk2(self):
        print("BHK2")

class Son(Father):
    btc="1BTC"

    def BHK3(self):
        print("BHK3")

s=Son()
f=Father()
gf=Grand_Father()