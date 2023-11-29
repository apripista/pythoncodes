# even and odd number checker in python
# you will be required to restart the
# program each time it finish the first execution.

while True:
    try:
        number = int(input("\nENTER A NUMBER: "))
        break
    except ValueError:
        print("INVALID NUMBER, ONLY INTEGERS ARE ALLOWED")

if number % 2 == 0:
    print(f"The number is even {number}.")
else:
    print(f"The number is odd {number}.")