import math

class Figure:
    def calculate_area(self):
        pass

class Rectangle(Figure):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * pow(self.radius, 2)

class Square(Figure):
    def __init__(self, side_length):
        self.side_length = side_length

    def calculate_area(self):
        return pow(self.side_length, 2)

class Triangle(Figure):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        return 0.5 * self.base * self.height

while True:
    figure = input("Enter the name of the figure (square, rectangle, circle, triangle), or type 'exit' to quit: ").lower()

    if figure == "exit":
        print("Exiting the program.")
        break

    if figure == "square":
        side_length = float(input("Enter the side length of the square: "))
        square = Square(side_length)
        area = square.calculate_area()
        print(f"The area of the square is {area}")
    elif figure == "rectangle":
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        rectangle = Rectangle(length, width)
        area = rectangle.calculate_area()
        print(f"The area of the rectangle is {area}")
    elif figure == "circle":
        radius = float(input("Enter the radius of the circle: "))
        circle = Circle(radius)
        area = circle.calculate_area()
        print(f"The area of the circle is {area}")
    elif figure == "triangle":
        base = float(input("Enter the base length of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        triangle = Triangle(base, height)
        area = triangle.calculate_area()
        print(f"The area of the triangle is {area}")
    else:
        print("Invalid figure. Please enter 'square', 'rectangle', 'circle', 'triangle', or 'exit'.")
