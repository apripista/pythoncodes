def calculate_gpa(grades):
    grade_points = {'A': 5, 'B+': 4, 'B': 3, 'C': 2, 'D': 1, 'F': 0}

    total_credits = len(grades)
    total_grade_points = sum(grade_points.get(grade, 0) for grade in grades)

    if total_credits == 0:
        return 0  # Avoid division by zero

    gpa = total_grade_points / total_credits
    return round(gpa, 2)  # Round to two decimal places


def get_user_grades(num_subjects):
    grade_points = {'A': 5, 'B+': 4, 'B': 3, 'C': 2, 'D': 1, 'F': 0}
    user_grades = []

    for _ in range(num_subjects):
        while True:
            grade_input = input(
                f"Enter the grade for subject {_ + 1} (A, B+, B, C, D, F): ").upper()
            if grade_input in grade_points:
                user_grades.append(grade_input)
                break
            else:
                print("Invalid grade. Please enter a valid grade.")

    return user_grades


# Ask the user for the number of subjects
while True:
    try:
        num_subjects = int(
            input("How many subjects do you have this semester? "))
        if num_subjects > 0:
            break
        else:
            print("Please enter a valid number of subjects (greater than 0).")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Get grades from the user
user_grades = get_user_grades(num_subjects)

# Calculate and print the GPA
gpa = calculate_gpa(user_grades)
print(f"The GPA is: {gpa}")
