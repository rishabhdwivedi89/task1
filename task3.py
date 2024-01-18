import mysql.connector

# Function to create a connection to the MySQL database
def create_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="school"
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

# Function to execute a query and fetch all results
def execute_query(connection, query):
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    return result

# Function to execute a query and commit changes
def execute_update_query(connection, query):
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    cursor.close()

# Function to create a table if not exists
def create_table(connection):
    query = """
    CREATE TABLE IF NOT EXISTS students (
        student_id INT AUTO_INCREMENT PRIMARY KEY,
        first_name VARCHAR(255),
        last_name VARCHAR(255),
        age INT,
        grade FLOAT
    )
    """
    execute_update_query(connection, query)

# Function to insert a new student record
def insert_student(connection, first_name, last_name, age, grade):
    query = f"""
    INSERT INTO students (first_name, last_name, age, grade)
    VALUES ('{first_name}', '{last_name}', {age}, {grade})
    """
    execute_update_query(connection, query)

# Function to update the grade of a student
def update_grade(connection, first_name, new_grade):
    query = f"""
    UPDATE students
    SET grade = {new_grade}
    WHERE first_name = '{first_name}'
    """
    execute_update_query(connection, query)

# Function to delete a student by last name
def delete_student(connection, last_name):
    query = f"""
    DELETE FROM students
    WHERE last_name = '{last_name}'
    """
    execute_update_query(connection, query)

# Function to fetch and display all student records
def fetch_and_display_students(connection):
    query = "SELECT * FROM students"
    students = execute_query(connection, query)

    if students:
        for student in students:
            print(student)
    else:
        print("No students found.")

if __name__ == "__main__":
    # Change the following values with your own database credentials
    db_connection = create_connection()

    if db_connection:
        create_table(db_connection)

        # Insert a new student record
        insert_student(db_connection, "Alice", "Smith", 18, 95.5)

        # Update the grade of the student with the first name "Alice"
        update_grade(db_connection, "Alice", 97.0)

        # Delete the student with the last name "Smith"
        delete_student(db_connection, "Smith")

        # Fetch and display all student records
        fetch_and_display_students(db_connection)

        # Close the database connection
        db_connection.close()
