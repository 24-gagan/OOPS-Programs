class Parent1:
    def func1(self):
        print("This is Parent1")
class Parent2:
    def func2(self):
        print("This is parent2")
class Child(Parent1,Parent2):
    def func3(self):
        print("This is child")

c=Child()
c.func1()
c.func2()
c.func3()