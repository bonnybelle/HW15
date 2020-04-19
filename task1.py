# Реализовать классы дескрипторы StaticMethod и ClassMethod.


class StaticMethod(object):
    def __init__(self, method):
        self.method = method

    def __get__(self, instance, owner):
        return self.method


class ClassMethod(object):
    def __init__(self, method):
        self.method = method

    def __get__(self, instance, owner):
        if owner is None:
            owner = type(instance)

        def new_func(*args):
            return self.method(owner, *args)
        return new_func
# -------------------------------------------------------


class MyClassForStaticMethod:
    @StaticMethod
    def multiplying(self, x):
        x *= 2
        return x


sm = MyClassForStaticMethod()
print('(static method)', sm.multiplying('self', 9), '\n')


class SomeClass:
    @classmethod
    def do_something(cls):
        print(cls.__name__)


class First(SomeClass):
    ...


class Second(SomeClass):
    pass


frst = First()
scnd = Second()
print('(class method) do_something: ', frst.do_something())
print('(class method) 01 do_something: ', scnd.do_something())
