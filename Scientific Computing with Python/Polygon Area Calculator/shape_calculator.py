class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return "Rectangle(width={}, height={})".format(self.width, self.height)

    def set_width(self, w):
        self.width = w

    def set_height(self, h):
        self.height = h

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        if self.width <= 50 and self.height <= 50:
            x = '*' * self.width + '\n'
            x *= self.height
        else:
            x = 'Too big for picture.'
        return x

    def get_amount_inside(self, shape):
        return int(self.width / shape.width) * int(self.height / shape.height)


class Square(Rectangle):
    def __init__(self, side):
        Rectangle.width = side
        Rectangle.height = side

    def __str__(self):
        return "Square(side={})".format(self.width)

    def set_side(self, value):
        Rectangle.set_width(self, value)
        Rectangle.set_height(self, value)
