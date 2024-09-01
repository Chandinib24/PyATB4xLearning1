Public_toilet="PB"

def Home():
    Private_toilet="PT"
    print(Private_toilet)
    Public_toilet = "LPB"
    print(Public_toilet) # we can reinitialize the public toilet value inside the function and then use
    #but before printing we should reinitialise , if reinitialised outside tthe function it is global or else it is local

Home()

def stranger():
    print(Public_toilet)

stranger()

print(Public_toilet)