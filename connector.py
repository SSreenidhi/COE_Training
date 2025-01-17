import mysql.connector as con

# Connect to the database
mydb = con.connect(
    host="localhost",
    user="root",
    password="1234",
    database="retail"
)
mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE IF NOT EXISTS students (sid INT, sname VARCHAR(20));")

mycursor.execute("INSERT INTO students (sid, sname) VALUES (1, 'John');")
mycursor.execute("INSERT INTO students (sid, sname) VALUES (2, 'Alice');")
mycursor.execute("INSERT INTO students (sid, sname) VALUES (3, 'Bob');")

mycursor.execute("UPDATE students SET sname = 'Alicia' WHERE sid = 2;")

mycursor.execute("DELETE FROM students WHERE sid = 1;")
mydb.commit()

print("3 records inserted successfully.")
print("1 record updated and 1 record deleted.")

mycursor.close()
mydb.close()
