class A:
    def method(self):
        print("This method belongs to class A")


class B(A):
    def method(self):
        print("This method belongs to class B")


class C(A):
    def method(self):
        print("This method belongs to class C")


class D(B, C):
    pass


d = D()
d.method()

# This program outlines the concept of the "Diamond Problem". Class B and C both inherit A, and class D inherits both B and C.
# In the event that B and C run a method of the same name, class D when it is run will prioritise running the method from the class that is listed first in it's inherited attributes
# General wisdom is to avoid multiple inheritance altogether, as the inheritance is non-obvious and creates fragile coupling between classes (which could become worrisome if B or C changed).
# It is a poor choice in code that will scale as this compounds the messiness and can make the code difficult to reason out
