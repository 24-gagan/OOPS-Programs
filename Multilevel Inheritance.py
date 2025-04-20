# Base class (Grandparent)
class Grandparent:
    def grandparent_method(self):
        print("This is Grandparent class")

# Derived class (Parent) inherits from Grandparent
class Parent(Grandparent):
    def parent_method(self):
        print("This is Parent class")

# Derived class (Child) inherits from Parent
class Child(Parent):
    def child_method(self):
        print("This is Child class")

# Creating an object of Child class
obj = Child()

# Calling methods from all classes
obj.grandparent_method()  # Output: This is Grandparent class
obj.parent_method()       # Output: This is Parent class
obj.child_method()        # Output: This is Child class
