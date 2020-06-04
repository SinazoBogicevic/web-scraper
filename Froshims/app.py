import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/registry", methods=["POST"])
def registry():
    name = request.form.get("name")
    studentNo = request.form.get("studentNo")
    mail = request.form.get("mail")
    dorm = request.form.get("dorm")

    if not name or not studentNo or not mail or not dorm:
        return "failure"
    else:
        try:
            with sqlite3.connect("studentsInfo.db") as conn:
                print("connected to table")
                cur = conn.cursor()
                cur.execute("INSERT INTO students VALUES(?, ?, ?, ?)",
                            (name, studentNo, mail, dorm))
                print("Inserted data successfully")
                conn.commit()
                print("Saved data successfully")
        except:
            conn.rollback()
            return "Failure"
        finally:
            conn = sqlite3.connect("studentsInfo.db")
            conn.row_factory = sqlite3.Row
            cur = conn.cursor()
            cur.execute("SELECT * from students")
            updatedList = cur.fetchall()
            return render_template("registry.html", updatedList=updatedList)
            conn.close()
