
def add_before_ui_after_ui(custom_function_where_we_want_extra_func):

    def wrapper(): # instead of wrapper we can use any other name
     print("Before running the UI TC")
     print("open the browser")
     custom_function_where_we_want_extra_func()
     print("After running the UI TC")
     print("close the browser")

    return wrapper()

@add_before_ui_after_ui
def test_ui():
    print("I will test the UI")

