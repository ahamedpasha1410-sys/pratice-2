class PassedStudentsIterator:
    def __init__(self, students):
        self.students = students
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.students):
            student = self.students[self.index]
            self.index += 1

            # Return only students with marks >= 50
            if student["marks"] >= 50:
                return student

        raise StopIteration


students = [
    {"id": 101, "name": "Alice", "marks": 85},
    {"id": 102, "name": "Bob", "marks": 42},
    {"id": 103, "name": "Charlie", "marks": 78},
    {"id": 104, "name": "David", "marks": 35},
    {"id": 105, "name": "Emma", "marks": 91},
]

print("Passed Students:")
for student in PassedStudentsIterator(students):
    print(
        f"ID: {student['id']}, "
        f"Name: {student['name']}, "
        f"Marks: {student['marks']}"
    )
