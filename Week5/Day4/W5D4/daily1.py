import math

class Circle:

    # init that uses only the radius
    def __init__(self, radius: int) -> None:
        self.radius = radius # 4
        self.diameter = radius * 2 # 8

    @classmethod
    def from_diameter(cls, diameter: int):
        return Circle(diameter//2) # 8 // 2 = 4
# Print the circle and get something nice
    def __str__(self):
        return f'Radius: {self.radius}, Diameter: {self.diameter}, Area: {self.area():.3f}'

# Compute the circle’s area
    def area(self):
        return math.pi * self.radius ** 2

# Be able to add two circles together
    def __add__(self, other_circle):
        result = Circle(self.radius + other_circle.radius)
        return result

# # Be able to compare two circles to see which is bigger '<' / '>' 
    def __gt__(self, other_circle) -> bool: # greater than - '>' 
        return self.area() > other_circle.area()

# Be able to compare two circles and see if there are equal
    def __eq__(self, other_circle) -> bool:
        return self.area() == other_circle.area()


circle1 = Circle(2)


print(dir(circle1))










# circle2 = Circle.from_diameter(8)

# circle3 = circle1 + circle2

# # print(circle1 > circle2)

# # Be able to put them in a list and sort them 
# circles = [circle3, circle1, circle2]

# def check_circles(circles_list: list) -> None:
#     for circle in circles_list:
#         print(circle)

# check_circles(circles)

# circles.sort()

# print("AFTER SORTING\n")
# check_circles(circles)

