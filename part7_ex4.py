scores = [70, 85, 60, 90, 45]

def calculate_total(scores):
    return sum(scores)

def calculate_average(scores):
    if len(scores) == 0:
        return 0
    return sum(scores) / len(scores)



def classify_grade(score):
    if score < 0 or score > 100:
        return "Invalid marks. Please enter a value between 0 and 100."
    elif score >= 80:
        return "Excellent"
    elif score >= 60:
        return "Good."
    elif score >= 40:
        return "You have passed the exam."
    else:
        return "You have failed the exam."

print(classify_grade(90))
print(classify_grade(55))
print(classify_grade(25))



def count_passed(scores):
    no_passed = 0
    for s in scores:
        if s >= 40:
            no_passed += 1
    return no_passed

print("Total:", calculate_total(scores))
print("Average:", calculate_average(scores))
print("No of passed:", count_passed(scores))
