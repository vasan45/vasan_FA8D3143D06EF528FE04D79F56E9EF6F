class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

def sort_students(student_list):
    # Sort the list of student objects based on CGPA in descending order
    sorted_students = sorted(student_list, key=lambda x: x.cgpa, reverse=True)
    return sorted_students

# Create a list of student objects
students = [
    Student("Sachin", "A001", 3.75),
    Student("Balaji", "B002", 3.9),
    Student("Babu", "C003", 3.6),
    Student("Mahesh", "D004", 3.8),
]

# Call the sort_students function to sort the list
sorted_students = sort_students(students)

# Display the sorted list of students
for student in sorted_students:
    print(f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}")
