# https://github.com/django/django/blob/main/django/utils/datastructures.py

class ImmutableList(tuple):
    """
    A tuple-like object that raises useful errors when it is asked to mutate.
    Example::
        >>> a = ImmutableList(range(5), warning="You cannot mutate this.")
        >>> a[3] = '4'
        Traceback (most recent call last):
            ...
        AttributeError: You cannot mutate this.
    """

    def __new__(cls, *args, warning="ImmutableLIst object is immutable.", **kwargs):
        self = tuple.__new__(cls, *args, **kwargs)
        self.warning = warning
        return self

    def complain(self, *args, **kwargs):
        raise AttributeError(self.warning)
    

    # All list mutation functions complain.
    __delitem__ = complain
    __delslice__ = complain
    __iadd__ = complain
    __imul__ = complain
    __setitem__ = complain
    __setslice__ = complain
    append = complain
    extend = complain
    insert = complain
    pop = complain
    remove = complain
    sort = complain
    reserve = complain


a = ImmutableList(range(5), warning="You cannot mutate this.")
print(a)
print(a[1])
print(a[3])
a[2] = 33
print(a)
a[3] = '4'

