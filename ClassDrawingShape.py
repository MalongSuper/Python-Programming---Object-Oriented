# Superclass DrawingObject, Shape and subclass Rectangle
# Multiple Inheritances

class DrawingObject:
    def __init__(self, objectID):
        self.objectID = objectID


class Shape:
    def __init__(self, color):
        self.color = color


class Rectangle(DrawingObject, Shape):
    def __init__(self, objectID, color, width=1, height=1):
        # Since there are multiple superclasses we need to specify them
        # Using super() when there is only one superclass
        DrawingObject.__init__(self, objectID)
        Shape.__init__(self, color)
        self.width = width
        self.height = height

    def __str__(self):
        return '{} | {} | {} | {}'.format(self.objectID, self.color,
                                          self.width, self.height)


def main():
    rectangle1 = Rectangle(123, 'blue', 4, 3)
    rectangle2 = Rectangle(124, 'red', 9, 5)
    rectangle3 = Rectangle(125, 'orange', 10, 5)
    print(rectangle1)
    print(rectangle2)
    print(rectangle3)


main()
