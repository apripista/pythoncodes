# Python Project that calculates the area and perimeter of the circle
print('\nA PYTHON PROJECT TO CALCULATE THE AREA AND PERIMETER OF A CIRCLE')
print("WHEN USER ENTER A RADIUS OF THE CIRCLE\n")
radius = float(input('Enter the radius of the circle: '))
PIE = 3.1425
area = PIE * radius * radius
circumference = 2 * PIE * radius
print(f'The circumference of the circle is {circumference}')
print(f"The area of the circle is {area}")
