# Program to find area and perimeter of
# square, rectangle, triangle, and circle

# Square
side = float(input("Enter side of square: "))

square_area = side * side
square_perimeter = 4 * side

print("\nSquare")
print("Area =", square_area)
print("Perimeter =", square_perimeter)


# Rectangle
l = float(input("\nEnter length of rectangle: "))
b = float(input("Enter breadth of rectangle: "))

rectangle_area = l * b
rectangle_perimeter = 2 * (l + b)

print("\nRectangle")
print("Area =", rectangle_area)
print("Perimeter =", rectangle_perimeter)


# Triangle
base = float(input("\nEnter base of triangle: "))
height = float(input("Enter height of triangle: "))
side1 = float(input("Enter first side: "))
side2 = float(input("Enter second side: "))
side3 = float(input("Enter third side: "))

triangle_area = 0.5 * base * height
triangle_perimeter = side1 + side2 + side3

print("\nTriangle")
print("Area =", triangle_area)
print("Perimeter =", triangle_perimeter)


# Circle
r = float(input("\nEnter radius of circle: "))

circle_area = 3.14 * r * r
circle_perimeter = 2 * 3.14 * r

print("\nCircle")
print("Area =", circle_area)
print("Perimeter =", circle_perimeter)
