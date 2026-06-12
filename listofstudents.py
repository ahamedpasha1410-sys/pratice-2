students = [
    ["Alice", 85],
    ["Bob", 92],
    ["Charlie", 78]
]

for student in SequenceIterator(students):
    name, marks = student
    print(f"{name} scored {marks}")
