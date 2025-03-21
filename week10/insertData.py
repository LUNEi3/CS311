import sqlite3

# insert = "INSERT INTO student VALUES (?, ?, ?, ?, ?, ?)"
conn = sqlite3.connect('db/db_week10.db')
cursor = conn.cursor()

select = "SELECT * FROM student"
cursor.execute(select)
data = cursor.fetchall()
length = len(data)
print(length)