"""Write a Python class named Student with two attributes student_id, student_name. Add a new attribute student_class. Create a function to display the entire attribute and their values in Student class.
Sample Input:
Enter Student Id : M11
Enter Student Name: Anusha Rao
Expected Output:
Original attributes and their values of the Student class:
Student ID: M11
Student Name: Anusha Rao"""

class Student:
    def __init__(self, student_id, student_name, student_class=None):
        self.student_id = student_id
        self.student_name = student_name
        self.student_class = student_class

    def display(self):
        print("Original attributes and their values of the Student class:")
        print(f"Student ID: {self.student_id}")
        print(f"Student Name: {self.student_name}")
        if self.student_class:
            print(f"Student Class: {self.student_class}")

student_id = input("Enter Student Id : ")
student_name = input("Enter Student Name: ")
student = Student(student_id, student_name)
student.display()
