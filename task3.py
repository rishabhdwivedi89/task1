import mysql.connector


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


def execute_query(connection, query):
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    return result


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


def insert_student(connection, first_name, last_name, age, grade):
    query = f"""
    INSERT INTO students (first_name, last_name, age, grade)
    VALUES ('{first_name}', '{last_name}', {age}, {grade})
    """
    execute_update_query(connection, query)


def update_grade(connection, first_name, new_grade):
    query = f"""
    UPDATE students
    SET grade = {new_grade}
    WHERE first_name = '{first_name}'
    """
    execute_update_query(connection, query)
def delete_student(connection, last_name):
    query = f"""
    DELETE FROM students
    WHERE last_name = '{last_name}'
    """
    execute_update_query(connection, query)


def fetch_and_display_students(connection):
    query = "SELECT * FROM students"
    students = execute_query(connection, query)

    if students:
        for student in students:
            print(student)
    else:
        print("No students found.")

if __name__ == "__main__":
    db_connection = create_connection()

    if db_connection:
        create_table(db_connection)

        
        insert_student(db_connection, "Alice", "Smith", 18, 95.5)

        
        update_grade(db_connection, "Alice", 97.0)

        
        delete_student(db_connection, "Smith")

        
        fetch_and_display_students(db_connection)

        
        db_connection.close()
