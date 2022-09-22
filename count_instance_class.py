class Meta(type):
    children_number = 0

    def __new__(cls, *args):
        instance = type.__new__(cls, *args)
        instance.class_number = cls.children_number
        cls.children_number = cls.children_number + 1
        return instance

    def __call__(cls, *args):
        instance = cls.__new__(cls)
        for arg in args:
            instance.__dict__[arg] = arg
        instance.class_number = cls.class_number
        return instance
    


Meta.children_number = 0

class Cls1(metaclass=Meta):
    def __init__(self, data):
        self.data = data


class Cls2(metaclass=Meta):
    def __init__(self, data):
        self.data = data

assert (Cls1.class_number, Cls2.class_number) == (0, 1)
a, b = Cls1(''), Cls2('')
assert (a.class_number, b.class_number) == (0, 1)