class Student:
    def __init__(self, student_id, name, grade):
        self.id = student_id
        self.name = name
        self.grade = grade

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Grade: {self.grade}"


class Teacher:
    def __init__(self, teacher_id, name, subject):
        self.id = teacher_id
        self.name = name
        self.subject = subject

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Subject: {self.subject}"


class SchoolManagementSystem:
    def __init__(self):
        self.students = []
        self.teachers = []

    def add_student(self):
        try:
            student_id = int(input("Enter Student ID: "))
            name = input("Enter Student Name: ")
            grade = input("Enter Student Grade: ")
            self.students.append(Student(student_id, name, grade))
            print("Student added successfully.")
        except ValueError:
            print("Invalid input. ID must be a number.")

    def add_teacher(self):
        try:
            teacher_id = int(input("Enter Teacher ID: "))
            name = input("Enter Teacher Name: ")
            subject = input("Enter Subject: ")
            self.teachers.append(Teacher(teacher_id, name, subject))
            print("Teacher added successfully.")
        except ValueError:
            print("Invalid input. ID must be a number.")

    def view_students(self):
        if not self.students:
            print("No student records found.")
        else:
            print("\nList of Students:")
            for student in self.students:
                print(student)

    def view_teachers(self):
        if not self.teachers:
            print("No teacher records found.")
        else:
            print("\nList of Teachers:")
            for teacher in self.teachers:
                print(teacher)

    def run(self):
        while True:
            print("\n--- School Management System ---")
            print("1. Add Student")
            print("2. Add Teacher")
            print("3. View All Students")
            print("4. View All Teachers")
            print("5. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.add_student()
            elif choice == '2':
                self.add_teacher()
            elif choice == '3':
                self.view_students()
            elif choice == '4':
                self.view_teachers()
            elif choice == '5':
                print("Exiting system. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    sms = SchoolManagementSystem()
    sms.run()
