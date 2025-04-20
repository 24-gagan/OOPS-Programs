class Parent:
    def show(self):
        print("This is Parent class")
class Child(Parent):
    def show(self):
        print("This is child class")
p=Parent()
c=Child()
p.show()
c.show()