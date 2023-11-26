# simple bmi calculator(bmi = Body Mass Index)

print("\nTHE SIMPLE BMI TO ASSIST DOCTORS IN HOSPITALS")

while True:  # trying to prevent invalid inputs by typo
    try:
        mass = float(input("Enter your weight in kg:  "))
        height_cm = float(input("Enter your height in cm:  "))
        break
    except ValueError:
        print("Invalid inputs")

height_m = height_cm / 100  # convert height in centimeter to meter
bmi = mass / (height_m * height_m)  # calculate the BMI
print(f"YOUR BMI IS {bmi:.2f}")

# specifying if a person has no obesity or otherwise
if bmi < 18.50:
    print("Underweight, seek medical help as soon as possible")
elif bmi <= 18.50 or bmi <= 24.90:
    print("Normal weight, please maintain your diet, sleep, work and exercises")
elif bmi <= 25 or bmi <= 29.9:
    print("Overweight, go to the gym to reduce your fat.")
elif bmi <= 30 or bmi <= 34.9:
    print("Your obesity is in class one")
elif 35 <= bmi < 39.9:
    print("Obesity class two")
else:
    print("Obesity class three")

