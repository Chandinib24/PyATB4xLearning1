from abc import ABC, abstractmethod

class ExcelReader():
    @abstractmethod
    def ReadfromeExcel(self):
        pass
class Browser(ExcelReader):

    @abstractmethod
    def start_Browser(self):
        pass
    @abstractmethod
    def stop_Browser(self):
        pass

class TC1(Browser):
    def start_Browser(self):
        print("Browser is started")
    def stop_Browser(self):
        print("Browser is stopped")
    def ReadfromeExcel(self):
        print("Excel is ready")

    def runTC(self):
        self.start_Browser()
        self.ReadfromeExcel()
        self.stop_Browser()
tc1=TC1()
tc1.runTC()