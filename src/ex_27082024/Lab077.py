import time


def time_decorator(func):
    def wrapper():
        start_time=time.time()
        print(start_time)
        func()
        end_time = time.time()
        print(end_time)
        print(f"Time taken by the function is {end_time-start_time}")
    return wrapper()

@time_decorator
def test_ui1():
    print("Add a function, time taken by this function")
    time.sleep(2)

@time_decorator
def test_ui2():
    print("Add a function, time taken by this function")
    time.sleep(5)

    #decorators are used to add extra functionalities
