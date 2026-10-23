def greet():
    print("Hello from UCSPyay!")

greet() 

def greet_student(name):
    print(f"Hello, {name}!")

greet_student("Aung Aung")
greet_student("Su Su")

def calculate_average(scores):
    if len(scores) == 0:
        return 0

    return sum(scores) / len(scores)

marks = [70, 80, 90]
result = calculate_average(marks)

print("Average:", result)