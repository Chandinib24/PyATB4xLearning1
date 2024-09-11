
class Bank:
    def __init__(self,account_number,balance):
      self.balance=balance
      self.__account_number=account_number

    def deposit(self,Amount):
        self.balance=self.balance+Amount

    def check_balance(self):
        print(self.balance)

    def show_me_accounr_number(self,is_auth):
        if is_auth==True:
            print(self.__account_number)
        else:
            print("Not allowed")

    def __internal_method(self):
        #advantage of private method is it can access the private variable as wella as it can also access the public method and protected
        #but this method is not allowed to access outside
        print("Private method")
        print(self.__account_number)
        print(self.show_me_accounr_number())


icici=Bank(1398747382,200)
icici.deposit(100)
icici.check_balance()
print(icici.show_me_accounr_number(True))
