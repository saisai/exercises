
def upper_attr(future_class_name, future_class_parents, future_class_attrs):
    """
    Return a class object, with the list of its attribute truned
    into uppercase.
    """
    uppercase_attrs = {
            attr if attr.startswith("__") else attr.upper(): v
            for attr, v in future_class_attrs.items()
            }
    # let `type` do the class creation
    return type(future_class_name, future_class_parents, uppercase_attrs)

__metaclass__ = upper_attr # this will affect all classes in the module

class Foo:
    bar = "bip"

print(hasattr(Foo, "bar"))
print(hasattr(Foo, "BAR"))
print(Foo.bar)

