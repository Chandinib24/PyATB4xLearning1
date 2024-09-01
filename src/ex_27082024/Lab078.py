# @staticmethod
# @classmethod
# @property
# @functools.wraps
#
# #all these are used in oops concept

#chaining decorators

def decorator1(func):
     def wrapper():
         print("Decorator1")
         func()
     return wrapper()


def decorator2(func):
    def wrapper():
        print("Decorator2")
        func()
    return wrapper()


@decorator1
@decorator2
def say_hello():
    print("hello!!")

say_hello()
