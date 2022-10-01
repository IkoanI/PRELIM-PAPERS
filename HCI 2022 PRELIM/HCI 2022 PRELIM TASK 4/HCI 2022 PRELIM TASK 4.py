from flask import Flask, render_template, request
import sqlite3
app = Flask(__name__)

@app.route('/')
def menu():
    return render_template("Task4_1.html")

@app.route('/student_health')
def records():
    conn = sqlite3.connect("students.db")
    records = conn.execute("SELECT Name, Gender, Weight, Height " +
                          "FROM Student " +
                          "LEFT JOIN StudentHealthRecord " +
                          "ON Student.StudentID = StudentHealthRecord.StudentID " +
                          "ORDER BY Gender ASC, Name DESC").fetchall()
    conn.close()
    return render_template("Task4_2.html", records = records)


@app.route("/statistics")
def stats():
    conn = sqlite3.connect("students.db")
    stats = conn.execute("SELECT Gender, COUNT(Gender), AVG(Weight), AVG(Height) " +
                         "FROM Student " +
                         "LEFT JOIN StudentHealthRecord " +
                         "ON Student.StudentID = StudentHealthRecord.StudentID " +
                         "GROUP BY Gender").fetchall()
    conn.close()
    return render_template("Task4_3.html", stats = stats)
    

@app.route("/add_record", methods = ["GET", "POST"])
def insert():
    if request.method == "POST":
        conn = sqlite3.connect("students.db")
        name = request.form.get("name")
        gender = request.form.get("gender")
        weight = request.form.get("weight")
        height = request.form.get("height")
        studentID = conn.execute("SELECT MAX(StudentID) " +
                                 "FROM Student").fetchone()[0]
        studentID = int(studentID) + 1

        conn.execute("INSERT INTO Student(Name, Gender) " +
                     "VALUES(?, ?)", (name, gender))
        
        conn.execute("INSERT INTO StudentHealthRecord " +
                     "VALUES(?, ?, ?)", (studentID, float(weight), float(height)))

        conn.commit()
        conn.close()
        return render_template("Task4_1.html")
        
    return render_template("Task4_4.html")
    
if __name__ == "__main__":
    app.run(debug = True)
