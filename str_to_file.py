# Numerical data to be stored
numbers = [1, 2, 3, 4, 5]

# Convert numerical values to strings
string_numbers = [str(num) for num in numbers]

# Join the converted strings with commas
data_to_write = ",".join(string_numbers)

# Open the file in write mode and write the data
with open('numbers.txt', 'w') as file_object:
    file_object.write(data_to_write)

print("Numerical data has been written to 'numbers.txt'")
