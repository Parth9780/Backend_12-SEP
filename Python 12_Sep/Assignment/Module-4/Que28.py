# What is used to check whether an object o is an instance of class A?

# isinstance() returns: True if the object is an instance or subclass of a class or any element of the tuple.

class A:
    pass
a = A()
isinstance(a, object)
True
isinstance(4, object)
True
isinstance("hello", object)
True
isinstance((1,), object)
True