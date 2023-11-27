width = int(input("Enter the width of the box: "))
height = int(input("Enter the height of the box: "))

print("*" * width)  # Print the top border

for _ in range(height - 2):
    print("*" + " " * (width - 2) + "*")  # Print the sides

print("*" * width)  # Print the bottom border
