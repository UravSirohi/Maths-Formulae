import operator
import math


def which_function():
    while True:
        which_function_ = input('''Which shape would you want to find area of input options are: circle, triangle, 
rectangle(including square), trapezium, parallelogram(including rhombus) and other(regular shape with over 4 
sides)?
>>>''')
        if which_function_ == 'circle':
            radius = float(input('Radius of the circle:'))
            print(f'Area of circle is {circle(radius)}')
        elif which_function_ == 'triangle':
            base = float(input('Base of the triangle: '))
            height = float(input('Height of the triangle: '))
            print(f'Area of triangle is {triangle(base, height)}')
        elif which_function_ == 'rectangle':
            width = float(input('Width of rectangle/square: '))
            length = float(input('Length of rectangle/square: '))
            print(f'Area of rectangle is {rectangle(width, length)}')
        elif which_function_ == 'trapezium':
            top_length = float(input('Top line length of trapezium: '))
            bottom_length = float(input('Bottom line length of trapezium: '))
            height = float(input('Height of trapezium'))
            print(f'Area of trapezium is {trapezium(top_length, bottom_length, height)}')
        elif which_function_ == 'parallelogram':
            height = float(input('Height of parallelogram/rhombus: '))
            length = float(input('Length of bottom line of parallelogram/rhombus: '))
            print(f'Area of parallelogram is {parallelogram(height, length)}')
        elif which_function_ == 'other':
            height = float(input('Height of regular polygon: '))
            side_length = float(input('Side length of regular polygon: '))
            number_of_sides = float(input('Number of sides of regular polygon: '))
            print(f'Area of other is {other(height, side_length, number_of_sides)}')
        else:
            print('Request unavailable')


def circle(radius):
    pi = math.pi
    area = operator.mul(operator.pow(radius, 2), pi)
    return area


def triangle(base, height):
    area = operator.truediv(operator.mul(base, height), 2)
    return area


def rectangle(width, length):
    return operator.mul(width, length)


def trapezium(top_length, bottom_length, height):
    area = operator.mul(operator.truediv(operator.add(top_length, bottom_length), 2), height)
    return area


def parallelogram(height, length):
    return operator.mul(height, length)


def other(height, side_length, number_of_sides):
    part_of_area = operator.truediv(operator.mul(operator.truediv(height, 2), side_length), 2)
    if number_of_sides < 4:
        raise Exception('Polygon must have at least 5 sides and must not be a decimal number of sides')
    area = operator.mul(part_of_area, number_of_sides)
    return area


which_function()
