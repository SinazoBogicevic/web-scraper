import sqlite3
conn = sqlite3.connect("studentsInfo.db")
print("Database opened successfully")

# create a table
conn.execute("CREATE TABLE students (id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR(255) NOT NULL, studentNo INTEGER NOT NULL, mail VARCHAR(255) NOT NULL, dorm VARCHAR(255) NOT NULL )")
print("Table created successfully")

# save the changes
conn.commit

# close the connection
conn.close()
