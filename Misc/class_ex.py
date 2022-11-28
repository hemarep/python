"""

"# class MyClass:
#     def __init__(self):
#         print("this is a constructor")
#     def func(self):
#         print("func :", self)
#
#     def stat_func(self):
#         print("static_func :", self)
#
# mc1 = MyClass()
# mc1.func()
# MyClass.func("arun")
# MyClass.stat_func("shankar")


class GrandParent():
    "This is the GrandParent class"

    def __init__(self):
        print("Constructor from Grand Parent")

    def GrandParentFunction(self,name):
        print("This is a message from the GrandParent.GrandParentFunction",name)

# This inherits the GrandParent class
class Parent():
    "This is the Parent class"

    def __init__(self):
        print("Constructor from Parent")

    def ParentFunction(self,name):
        print("This is a message from the Parent.ParentFunction", name)

# Class that inherits Parent Class
class Child(Parent,GrandParent):
    "This is the ChildMI, this inherits Parent_1 and Parent_2"

    def __init__(self):
        print("Constructor from Child")

    def ChildFunction(self, name):
        print("This is a message from the Child.ChildFunction", name)

# Create ChildMI Object
gcObj = Child()

gcObj.GrandParentFunction("munuswamy")
gcObj.ParentFunction("arun")
gcObj.ChildFunction("adhyu")
"""

class Emp:
    def __init__(self, eid,name,sal):
        self.eid = eid
        self.name = name
        self.sal = sal
    def disp(self):
        print(self.eid,self.name,self.sal)
    def __str__(self):
        return(self.name)
    
e1=Emp(101,"arun",1000000)
e1.disp()
print(e1)