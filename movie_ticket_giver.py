ticket = "unknown"

try:
    age = int(input("Enter your age: "))
    if age < 0:
        print("No such age. please put a valid age.")
    elif age < 3:
        ticket = 'free'
    elif 3 <= age < 12:
        ticket = 10
    else:
        ticket = 15
    print(f"Your ticket cost is ${ticket}")
except ValueError:
    print("Invalid age format.")
