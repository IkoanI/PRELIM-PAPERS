from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    conn = sqlite3.connect("invigilation.db")
    teachers = conn.execute("SELECT Name FROM Teacher ORDER BY Name ASC").fetchall()
    result = []
    for teacher in teachers:
        roles = conn.execute("SELECT DISTINCT ExamDuty.'Role' " +
                             "FROM ExamDuty, Teacher " +
                             f"WHERE Teacher.Name = '{teacher[0]}' " +
                             "AND ExamDuty.TeacherID = Teacher.TeacherID " +
                             "ORDER BY ExamDuty.'Role' ASC").fetchall()
        for role in roles:
            count = conn.execute("SELECT COUNT(ExamDuty.Role) " +
                                 "FROM ExamDuty, Teacher " +
                                 f"WHERE Teacher.Name = '{teacher[0]}' " +
                                 "AND ExamDuty.TeacherID = Teacher.TeacherID " +
                                 f"AND ExamDuty.'Role' = '{role[0]}'").fetchone()

            result.append([teacher[0], role[0], count[0]])

    conn.close()
    return render_template("home.html", result = result)

@app.route('/schedule/<name>')
def schedule(name):
    conn = sqlite3.connect("invigilation.db")
    result = conn.execute("SELECT ExamSession.SubjectName, ExamSession.PaperNo, " +
                          "ExamDuty.'Role', Venue.VenueName, ExamSession.'Date', " +
                          "ExamSession.StartTime, ExamSession.EndTime " +
                          "FROM ExamDuty, ExamSession, Venue, Teacher " +
                          f"WHERE Teacher.Name = '{name}' " +
                          "AND ExamDuty.TeacherID = Teacher.TeacherID " +
                          "AND ExamSession.ExamSessionID = ExamDuty.ExamSessionID " +
                          "AND Venue.VenueID = ExamSession.VenueID " +
                          "ORDER BY ExamSession.'Date', ExamSession.StartTime ASC").fetchall()
    
    return render_template("schedule.html", name = name, result = result)
    

if __name__ == "__main__":
    app.run(debug = "True")
