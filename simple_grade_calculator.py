print("\nA PROGRAM THAT ALLOW STUDENTS TO CALCULATE THEIR GRADES IN SCHOOL")
while True:
    try:
        marks = float(input("Enter your marks: "))
        break
    except ValueError:
        print("NO SUCH MARKS. TYPO")

if marks < 0:
    print("We do not have that grade")
if 0 < marks <= 30:
    print("Grade F")
elif 30 < marks <= 40:
    print("Grade D")
elif 40 < marks <= 50:
    print("Grade C")
elif 50 < marks <= 60:
    print("Grade B")
elif 60 < marks <= 69:
    print("Grade B+")
elif 69 < marks <= 100:
    print("Grade A")
