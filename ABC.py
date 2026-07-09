# Abstract Base Class
# Forces implementation of a certain rule within it's derived classes

from abc import ABCMeta, abstractmethod

# Since we have made this class an abstract class, we cannot now instantiate objects for this class. It can only be inherited by derived classes


class Shape(metaclass=ABCMeta):
    @abstractmethod
    def area(self):
        return 0


class Square(Shape):
    side = 4

    def area(self):
        print(f"Area of square: {self.side * self.side}")


class Rectangle(Shape):
    length = 5
    breadth = 10

    def area(self):
        print(f"Area of rectangle: {self.length * self.breadth}")


square = Square()
rectangle = Rectangle()
square.area()
rectangle.area()
