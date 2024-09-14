#Custom exception-own

class BalanceLowException(Exception):
    def __init__(self,message):
        self.message=message
        super().__init__(message)

balance=100
withdraw=int(input("Enter the amount you eant to withdraw!! \n"))
if withdraw>balance:
    raise BalanceLowException("Balance is low")
else:
    print("Remaining Balance",(balance-withdraw))
#MyCustomException: Balance is low
