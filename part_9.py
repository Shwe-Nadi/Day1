student = {
    "name": "Ma Ma",
    "age": 21,
    "score": 88,
    "passed": True
}

print(student["name"])
print(student["score"])

students = [
    {"name": "Aung Aung", "score": 92},
    {"name": "Kyaw Kyaw", "score": 78},
    {"name": "Zin Zin", "score": 95}
]

for student in students:
    print(student["name"], student["score"])