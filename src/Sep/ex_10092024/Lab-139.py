class XYZ:
    def f1(self):
        try:
            a=int(input("Enter a number \n"))
        except Exception as e:
            print("Enter a print only value of a")
        else:
            print("a")
        finally:
            print("FINALLY:Any how i will be printed")
x=XYZ()
x.f1()

