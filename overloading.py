class Square:
    def __init__(self, side):
        self.side = side

    def __add__(square_one, square_two):
        # __add__ is a dunder method Python calls automatically whenever "+" is used between two Square objects
        # This lets us define what "+" should actually mean for this class (here, sum of perimeters) and allows objects in this class to behave intuitively the same way built-in types do (like integers and strings)
        return ((4*square_one.side)+(4*square_two.side))


square_one = Square(5)
square_two = Square(10)
# Without __add__ defined, "square_one + square_two" would raise a TypeError, since Python has no built-in idea of what "+" means for a custom class
print(f"The sum of sides of both the squares = {square_one + square_two}")
