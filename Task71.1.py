def calculate_area(length, width):
    area = length * width
    return area

def calculate_perimeter(length, width):
    perimeter = 2 * (length + width)
    return perimeter

def rectangle_info(length, width):
    area = calculate_area(length, width)
    perimeter = calculate_perimeter(length, width)

    print(f"Rectangle Area: {area}")
    print(f"Rectangle Perimeter: {perimeter}")
    
rectangle_info(4, 5)




