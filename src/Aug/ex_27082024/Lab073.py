
def outer_function():
    var1=30

    def innner_function():
        print(var1)

    def inner_function2():
        print(var1)
    innner_function()
    inner_function2()

outer_function()