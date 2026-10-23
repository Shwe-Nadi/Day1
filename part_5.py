marks = float(input("Enter your marks: "))

if marks >= 40:
    print("You have passed the exam.")
else:
    print("You have failed the exam.")

mark = float(input("Enter your marks: "))

if mark < 0 or mark > 100:
    print("Invalid marks. Please enter a value between 0 and 100.")
elif mark >= 80:
    print("Excellent")
elif mark >= 60:
    print("Good.")
elif mark >= 40:
    print("You have passed the exam.")
else:
    print("You have failed the exam.")