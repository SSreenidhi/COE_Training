"""Write a python script to enter student number, name, marks in c, c++ and java calculate and display total marks, average,
 result and grade. Print fail if student average is less than 70.  """
student_number = input("Enter student number: ")
student_name = input("Enter student name: ")
marks_c = float(input("Enter marks in C: "))
marks_cpp = float(input("Enter marks in C++: "))
marks_java = float(input("Enter marks in Java: "))
total_marks = marks_c + marks_cpp + marks_java
average = total_marks / 3
if average >= 70:
    result = "Pass"
    if average >= 90:
        grade = "A"
    elif average >= 80:
        grade = "B"
    else:
        grade = "C"
else:
    result = "Fail"
    grade = "N/A"
print("\nStudent Details:")
print(f"Student Number: {student_number}")
print(f"Student Name: {student_name}")
print(f"Total Marks: {total_marks}")
print(f"Average Marks: {average}")
print(f"Result: {result}")
print(f"Grade: {grade}")
