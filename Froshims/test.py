import sqlite3 as lite
msg = ""

try:
    with lite.connect("studentsInfo.db") as conn:
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO students VALUES('Sour', 4546, 'worms@school.com', 'Erica')")
        conn.commit()
        print("data saved")
        msg = "Successfully inserted"
except:
    conn.rollback()
    msg = "Error"
finally:
    conn.close()
    print(msg)
