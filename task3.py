# Реализовать дескриптор валидации для атрибута email.
# Ваш дескриптор должен проверять формат email который вы пытаетесь назначить.


def is_valid_email(test_email):
    check_symbols = '\\ / \' \",!#$%^&*":~`+<([{}])>'
    if '@' in test_email:
        left_part = test_email.split('@')[0]
        if 3 < len(left_part) < 25 and check_symbols not in test_email:
            return True
        else:
            raise Exception('invalid email')


class EmailDescriptor(object):
    def __get__(self, instance, owner):
        print('getting...')
        return instance.__dict__.get('email')

    def __set__(self, instance, value):
        print('setting...')
        if is_valid_email(value):
            instance.__dict__['email'] = value

    def __delete__(self, instance):
        print('deleting...')
        if instance.__dict__ is None:
            raise AttributeError('can`t delete attribute')
        instance.__dict__ = None


class MyClass(object):
    email = EmailDescriptor()


mc = MyClass()
mc.email = 'validemail@gmail.com'
print(mc.email)

mc1 = MyClass()
mc1.email = 'i&n#va$lidemail'
print(mc1.email)

mc2 = MyClass()
mc2.email = 'bademail'
print(mc2.email)
