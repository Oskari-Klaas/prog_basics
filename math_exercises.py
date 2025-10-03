"""Math exercises."""
import math


def sum_and_difference(num_a: int, num_b: int) -> tuple:
    """Return the sum and difference of given variables num_a and num_b."""
    sum = num_a + num_b
    difference = num_a - num_b
    return sum, difference


def float_division(num_a: int, num_b: int) -> float:
    """Divide given variables num_a and num_b and return the result."""
    division = num_a / num_b
    return division


def integer_division(num_a: int, num_b: int) -> int:
    """Divide given variables num_a and num_b and return the result rounded down."""
    division = num_a // num_b
    return division


def powerful_operations(num_a: int, num_b: int) -> tuple:
    """Return the product of given variables, num_a to the power of num_b and the remainder of division of variables."""
    multiply_numbers = num_a * num_b
    power = num_a ** num_b
    remainder = num_a % num_b
    return multiply_numbers, power, remainder


def find_average(num_a: int, num_b: int) -> float:
    """Return the average of given variables."""
    average = (num_a + num_b) / 2
    return average


def area_of_a_circle(radius: float) -> float:
    """Calculate and return the area of a circle."""
    circle_area = math.pi * radius ** 2
    circle_area = round(circle_area, 2)
    return circle_area


def area_of_an_equilateral_triangle(side_length: float) -> int:
    """Calculate and return the area of an equilateral triangle."""
    triangle_area = math.sqrt(3) / 4 * side_length ** 2
    triangle_area = round(triangle_area)
    return triangle_area


def calculate_discriminant(a: int, b: int, c: int) -> int:
    """Calculate discriminant with given variables and return the result."""
    discriminant = b ** 2 - 4 * a * c
    return discriminant


def calculate_hypotenuse_length(a: int, b: int) -> float:
    """Return the length of hypotenuse when the lengths of the catheti are given."""
    c = math.sqrt(a ** 2 + b ** 2)
    return c


def calculate_cathetus_length(a: int, c: int) -> float:
    """Return the length of cathetus when the lengths of the second cathetus and hypotenuse are given."""
    b = math.sqrt(c ** 2 - a ** 2)
    return b

# 11

seconds = 29292
minutes = seconds // 60
hours = minutes // 60
minutes = minutes % 60
print(f"{seconds} sekundit on {hours} tund(i) ja {minutes} minut(it).")

# 12

angle = 30
sine = math.sin(math.radians(angle))
sine = round(sine, 1)
cosine = math.cos(math.radians(angle))
cosine = round(cosine, 1)
print(f"Nurk: {angle}, siinus: {sine}, koosinus: {cosine}.")

# 13

n = 5
lots_of_heys = n * "Hey"
print(lots_of_heys)

# 14

num_a = 5
num_b = 3
string_numbers = str(num_a) + str(num_b)
print(string_numbers)
