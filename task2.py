# Создать свой тип с помощью type.


def my_function(self, x):
    print('function: ', self.__list__)
    x = x ** x
    return x


MyClass = type('MyClass',
               (object,),
               {'first_key': 'first value', 'call_to_function': my_function,
                '__list__': ['__list__ element №1', '__list__ element №2']}
               )
mc = MyClass()
print(MyClass.first_key)
print(mc.call_to_function(6))


'''
def func(self, *args):
    print('func: ', self.__dict__)
    return args


MyClass = type(
    'MyClass',
    (object,),
    {'a1': 1, 'f1': func, '__dict__': {'a2': 2}}
)

mc = MyClass()
print(MyClass.a1)
print(mc.f1())
'''
