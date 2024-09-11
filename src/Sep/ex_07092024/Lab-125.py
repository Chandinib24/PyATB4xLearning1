from abc import ABC, abstractmethod

class Gearbox():
    @abstractmethod
    def setgear(self):
        pass
class Engine():

    @abstractmethod
    def start(self):
        pass
    @abstractmethod
    def stop(self):
        pass

class Car(Engine):
    def start(self):
        print("starting")
    def setgear(self):
        print("gearbox is ready")
    def stop(self):
        print("stopping")

    def drive(self):
        self.start()
        self.setgear()
        self.stop()
car=Car()
car.drive()