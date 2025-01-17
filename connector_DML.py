import mysql.connector as con

mydb = con.connect(
  host="localhost",
  user="root",
  password="1234",
  database="retail"
)

mycursor = mydb.cursor()
sname = input("Enter student name: ")
sid = input("Enter student ID: ")

mycursor.execute("INSERT INTO students (sid, sname) VALUES (%s, %s)", (sid, sname))
mycursor.execute("select * from students")
students=mycursor.fetchall();
for std in students:
    print(std)

mydb.commit()

print(f"Record for student {sname} (ID: {sid}) has been inserted successfully.")
