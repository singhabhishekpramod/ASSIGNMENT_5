def create_student_dict():
    students = {
        "John": 85,
        "Alice": 90,
        "Bob": 78,
        "Charlie": 92,
        "David": 88
    }
    return students

def get_student_marks(students):
    student_name = input("Enter the student's name: ")
    if student_name in students:
        print(f"{student_name}'s marks: {students[student_name]}")
    else:
        print(f"Student '{student_name}' not found.")

def main():
    students = create_student_dict()
    print("Student Dictionary:")
    for student, marks in students.items():
        print(f"{student}: {marks}")
    get_student_marks(students)

if __name__ == "__main__":
    main()

