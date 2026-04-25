import mysql.connector

# Connect to MySQL server
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Pratham@1968"
)

cursor = conn.cursor()

# Create database
cursor.execute("CREATE DATABASE IF NOT EXISTS proxy_attendance")

# Use database
cursor.execute("USE proxy_attendance")

# Create students table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    student_id VARCHAR(50),
    face_encoding TEXT
)
""")

# Create attendance table
cursor.execute("""
CREATE TABLE IF NOT EXISTS attendance (
    id INT AUTO_INCREMENT PRIMARY KEY,
    student_id VARCHAR(50),
    name VARCHAR(100),
    date DATE,
    time TIME
)
""")

print("Database and tables created successfully!")

conn.commit()
conn.close()