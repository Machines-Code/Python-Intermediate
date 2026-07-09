class Square:
    def __init__(self, side):
        self.side = side

    def __pow__(square_one, square_two):
        return (square_one ** square_two)


square_one = Square(2)
square_two = Square(4)

print(
    f"Side of square one to the power of side of square two: {square_one.side ** square_two.side}")
