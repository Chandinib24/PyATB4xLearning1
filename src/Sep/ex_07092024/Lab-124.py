
from abc import ABC, abstractmethod

class PyATB():

    @abstractmethod
    def payfee(self):
     pass

    def enrolled(self):
        print("Enrolled")

class Amit(PyATB):
    def payfee(self):
        print("paid")

shubam=Amit()
shubam.payfee()