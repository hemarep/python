class GrandParent():
    X=10
    def __init__(self):
        print("Constructor from Grand Parent")
    def GrandParentFunction(self):
        print("This is a message from the GrandParent.GrandParentFunction")

class Parent1(GrandParent):
    X = 100
    def __init__(self):
        print("This is a message from ", Parent1.__name__)
    def func1(self):
        print("This is a message from Parent1.func1")
        super().GrandParentFunction()

class Child1(Parent1):
    X = 999
    def __init__(self):
        super().__init__()
        print(super().X)
        print(self.X)
        print("This is a message from Child1 constructor")

    def func1(self):
        print("This is a message from Child1.func1")
    def func2(self):
        super().func1()

supObject = Child1()
supObject.func1()
supObject.func2()
# MARKDOWN ```