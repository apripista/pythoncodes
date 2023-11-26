# Python Project that calculates the area and perimeter of the circle
# from user inputs

try:
    def rectangle_properties(length, width):
        """function to find the area and perimeter of a rectangle"""
        area = length * width
        perimeter = 2 * (length + width)
        return area, perimeter

    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))

    area_result, perimeter_result = rectangle_properties(length, width)
    print(f"\n{area_result:.2f} is the area of the rectangle")
    print(f"{perimeter_result:.2f} is the perimeter of the rectangle")

except ValueError:
    print("Invalid format")
