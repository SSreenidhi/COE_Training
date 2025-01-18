import mysql.connector as con

mydb = con.connect(
    host="localhost",
    user="root",
    password="1234",
    database="restaurant"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE IF NOT EXISTS customers (customer_id INT PRIMARY KEY,customer_name VARCHAR(255),phone_number VARCHAR(15),bill_amount DECIMAL(10, 2));")

def insert_customer():
    customer_name = input("Enter customer name: ")
    customer_id = input("Enter customer ID: ")
    phone_number = input("Enter phone number: ")
    bill_amount = input("Enter bill amount: ")

    mycursor.execute("INSERT INTO customers (customer_id, customer_name, phone_number, bill_amount) VALUES (%s, %s, %s, %s)",(customer_id, customer_name, phone_number, bill_amount))
    mydb.commit()
    print(f"Record for customer {customer_name} (ID: {customer_id}) has been inserted successfully.")


def delete_customer():
    customer_id = input("Enter customer ID to delete: ")
    mycursor.execute("DELETE FROM customers WHERE customer_id = %s", (customer_id,))
    mydb.commit()
    print(f"Customer with ID {customer_id} has been deleted.")


def update_customer():
    customer_id = input("Enter customer ID to update: ")
    new_phone_number = input("Enter new phone number: ")
    new_bill_amount = input("Enter new bill amount: ")

    mycursor.execute("UPDATE customers SET phone_number = %s, bill_amount = %s WHERE customer_id = %s",(new_phone_number, new_bill_amount, customer_id))
    mydb.commit()
    print(f"Details for customer ID {customer_id} have been updated.")


def display_customers():
    mycursor.execute("SELECT * FROM customers")
    customers = mycursor.fetchall()
    for customer in customers:
        print(customer)


def additional_operations():
    print("1. Display total revenue")
    print("2. Count customers")
    choice = input("Enter your choice: ")

    if choice == "1":
        mycursor.execute("SELECT SUM(bill_amount) FROM customers")
        total_revenue = mycursor.fetchone()[0]
        print(f"Total revenue: {total_revenue}")

    if choice == "2":
        mycursor.execute("SELECT COUNT(*) FROM customers")
        customer_count = mycursor.fetchone()[0]
        print(f"Total number of customers: {customer_count}")


while True:
    print("\n1. Insert customer")
    print("2. Delete customer")
    print("3. Update customer")
    print("4. Display all customers")
    print("5. Additional operations")
    print("6. Exit")
    option = input("Enter your option: ")

    if option == "1":
        insert_customer()
    elif option == "2":
        delete_customer()
    elif option == "3":
        update_customer()
    elif option == "4":
        display_customers()
    elif option == "5":
        additional_operations()
    elif option == "6":
        break
    else:
        print("Invalid option. Please try again.")
