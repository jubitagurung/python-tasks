import math

def calculate_hypotenuse(side1, side2):
    hypotenuse = math.sqrt(side1**2 + side2**2)
    return hypotenuse

def triangle_info(side1, side2):
    hypotenuse = calculate_hypotenuse(side1, side2)
    print(f"The hypotenuse of the right triangle with sides {side1} and {side2} is {hypotenuse:.2f}")

# Test the function
triangle_info(4, 5)
