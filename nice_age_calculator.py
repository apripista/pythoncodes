# age calculate user need to input their
# birthdate in this format YYYY-MM-DD now for
# example birthdate may be 2000 year 4 april, and 2nd
# so you will be neede to enter it like this: 2000-04-02

from datetime import datetime


def calculate_age(birthdate, current_date):
    try:
        birthdate_obj = datetime.strptime(birthdate, "%Y-%m-%d")
        current_date_obj = datetime.strptime(current_date, "%Y-%m-%d")

        age = current_date_obj.year - birthdate_obj.year - (
            (current_date_obj.month, current_date_obj.day) < (birthdate_obj.month, birthdate_obj.day))
        return age
    except ValueError:
        return "Invalid date format"


print('Hey!, When prompted to enter your aga please')
print('follow the given format example birth date is: 1st Jan 2000.')
print('You should Enter it as 2000-01-01. That is year, month, and date')
current_date = datetime.now().strftime("%Y-%m-%d")
print(f"Current date is {current_date}")

# User input
birthdate = input("Enter your birthdate (YYYY-MM-DD): ")

age = calculate_age(birthdate, current_date)
if isinstance(age, int):
    print(f"Your age is: {age} years")
else:
    print(age)
