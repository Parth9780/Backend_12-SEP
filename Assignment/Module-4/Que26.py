# Explain Inheritance in Python with an example? What is init? Or What Is A Constructor In Python?
"""
--> Inheritance allows us to define a class that inherits all the methods and properties from another class. Parent class is the class being inherited from, also called base class. Child class is the class that inherits from another class, also called derived class.

--> Inheritance allows us to define a class that inherits all the methods and properties from another class.

--> Parent class is the class being inherited from, also called base class.

--> Child class is the class that inherits from another class, also called derived class.

        Class BaseClass:
            {Body}
        Class DerivedClass(BaseClass):
            {Body}
"""

class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

class Student(Person):
    pass

x = Student("Mike", "Olsen")
x.printname()
