import math

def calculate_hypotenuse(side1, side2):
    hypotenuse = math.sqrt(side1**2 + side2**2)
    return hypotenuse

def triangle_info(side1, side2):
    hypotenuse = calculate_hypotenuse(side1, side2)
    print(f"The length of the hypotenuse is: {hypotenuse:.2f}")
triangle_info(4, 5)
