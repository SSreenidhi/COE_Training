"""Write a program to calculate the hypotenuse of a right angled triangle

Note: you should use Math Module"""

import math

def calculate_hypotenuse(a, b):
    return math.sqrt(a**2 + b**2)

side_a = float(input("Enter the length of side a: "))
side_b = float(input("Enter the length of side b: "))

hypotenuse = calculate_hypotenuse(side_a, side_b)

print("The length of the hypotenuse is:", hypotenuse)

