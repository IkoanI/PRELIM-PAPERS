from flask import Flask, render_template, request
import sqlite3
from datetime import datetime, timedelta

app = Flask(__name__)

@app.route('/')
def menu():
    return render_template("menu.html")

@app.route('/loan', methods = ["GET", "POST"])
def loan():
    if request.method == "POST":
        conn = sqlite3.connect("SportsLoans.db")
        name = request.form.get("name")
        equipment = request.form.get("equipment")
        quantity = request.form.get("qty")
        LoanDate = request.form.get("start")

        result = conn.execute("SELECT Equipment.ID, Student.ID, Equipment.Points " +
                              "FROM Student, Equipment " +
                              f"WHERE Student.Name = '{name}' " +
                              f"AND Equipment.Name = '{equipment}'").fetchone()

        (EqptID, StudentID, Points) = result
        startDate = datetime.strptime(LoanDate, "%Y-%m-%d")
        endDate = startDate + timedelta(days=2)
        ReturnDate = datetime.strftime(endDate, "%Y-%m-%d")

        for i in range(int(quantity)):
            conn.execute("INSERT INTO Loan(EqptID, StudentID, LoanDate, ReturnDate) "+
                         "VALUES(?, ?, ?, ?)", (EqptID, StudentID, LoanDate, ReturnDate))

        pointsEarned = int(Points) * int(quantity)
        conn.commit()
        conn.close()
        return render_template("success.html", name = name, ReturnDate = ReturnDate, pointsEarned = pointsEarned)

    conn = sqlite3.connect("SportsLoans.db")
    names = conn.execute("SELECT Name " +
                         "FROM Student " +
                         "ORDER BY Name ASC").fetchall()

    equipments = conn.execute("SELECT Name " +
                              "FROM Equipment " +
                              "ORDER BY Name ASC").fetchall()
    conn.close()
    return render_template("loan.html", names = names, equipments = equipments)

@app.route('/leaderboard', methods = ["GET", "POST"])
def leaderboard():
    if request.method == "POST":
        name = request.form.get("name")
        conn = sqlite3.connect("SportsLoans.db")
        studentPoint = conn.execute("SELECT SUM(Equipment.Points) " +
                                    "FROM Loan " +
                                    "INNER JOIN Equipment " +
                                    "ON Equipment.ID = Loan.EqptID " +
                                    "INNER JOIN Student " +
                                    "ON Loan.StudentID = Student.ID " +
                                    f"WHERE Student.Name = '{name}';").fetchone()
        
        leaderboard = conn.execute("SELECT Student.Name, SUM(Equipment.Points)" +
                                   "FROM Loan " +
                                   "INNER JOIN Student " +
                                   "ON Loan.StudentID = Student.ID " +
                                   "INNER JOIN Equipment " +
                                   "ON Loan.EqptID = Equipment.ID " +
                                   "GROUP BY Student.Name " +
                                   "ORDER BY SUM(Equipment.Points) DESC " +
                                   "LIMIT 3").fetchall()

        return render_template("leaderboard.html", studentPoint = studentPoint, leaderboard = leaderboard)
        
    return render_template("leaderboard.html", noName = True)

if __name__ == "__main__":
    app.run(debug = True)
