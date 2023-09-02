class MetaMemberControl(type):
    __slots__ = ()

    @classmethod
    def __prepare__(mcs, f_cls_name, f_cls_parents,  # f_cls means: future class
                    meta_args=None, meta_options=None):  # meta_args and meta_options is not necessarily needed, just so you know.
        f_cls_attr = dict()
        if not "do something or if you want to define your cool stuff of dict...":
            return dict(make_your_special_dict=None)
        else:
            return f_cls_attr

    def __new__(mcs, f_cls_name, f_cls_parents, f_cls_attr,
                meta_args=None, meta_options=None):

        original_getattr = f_cls_attr.get('__getattribute__')
        original_setattr = f_cls_attr.get('__setattr__')

        def init_getattr(self, item):
            if not item.startswith('_'):  # you can set break points at here
                alias_name = '_' + item
                if alias_name in f_cls_attr['__slots__']:
                    item = alias_name
            if original_getattr is not None:
                return original_getattr(self, item)
            else:
                return super(eval(f_cls_name), self).__getattribute__(item)

        def init_setattr(self, key, value):
            if not key.startswith('_') and ('_' + key) in f_cls_attr['__slots__']:
                raise AttributeError(f"you can't modify private members:_{key}")
            if original_setattr is not None:
                original_setattr(self, key, value)
            else:
                super(eval(f_cls_name), self).__setattr__(key, value)

        f_cls_attr['__getattribute__'] = init_getattr
        f_cls_attr['__setattr__'] = init_setattr

        cls = super().__new__(mcs, f_cls_name, f_cls_parents, f_cls_attr)
        return cls


class Human(metaclass=MetaMemberControl):
    __slots__ = ('_age', '_name')

    def __init__(self, name, age):
        self._name = name
        self._age = age

    def __getattribute__(self, item):
        """
        is just for IDE recognize.
        """
        return super().__getattribute__(item)

    """ with MetaMemberControl then you don't have to write as following
    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age
    """


def test_demo():
    human = Human('Carson', 27)
    # human.age = 18  # you can't modify private members:_age  <-- this is defined by yourself.
    # human.k = 18  # 'Human' object has no attribute 'k'  <-- system error.
    age1 = human._age  # It's OK, although the IDE will show some warnings. (Access to a protected member _age of a class)

    age2 = human.age  # It's OK! see below:
    """
    if you do not define `__getattribute__` at the class of Human,
    the IDE will show you: Unresolved attribute reference 'age' for class 'Human'
    but it's ok on running since the MetaMemberControl will help you.
    """


if __name__ == '__main__':
    test_demo()


# https://stackoverflow.com/questions/100003/what-are-metaclasses-in-python
