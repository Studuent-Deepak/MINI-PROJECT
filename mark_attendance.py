import mysql.connector
from datetime import datetime

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Pratham@1968",
    database="proxy_attendance"
)

cursor = conn.cursor()

name = "Prathmesh"
student_id = "CSE001"

now = datetime.now()

date = now.strftime("%Y-%m-%d")
time = now.strftime("%H:%M:%S")

sql = """
INSERT INTO attendance (student_id, name, date, time)
VALUES (%s, %s, %s, %s)
"""

values = (student_id, name, date, time)

cursor.execute(sql, values)

conn.commit()

print("Attendance marked successfully!")

conn.close()