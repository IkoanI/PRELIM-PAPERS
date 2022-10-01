from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/')
def menu():
    return render_template("menu.html")

@app.route('/latecomers')
def latecomers():
    conn = sqlite3.connect("Task4.db")
    latecomers = conn.execute("SELECT Name, Time FROM Person, Record \
                                WHERE Type = 'entry' AND Time > '0730' \
                                ORDER BY Record.Date ASC;").fetchall()
    return render_template("latecomers.html", latecomers = latecomers)

@app.route('/form')
def form():
    return render_template("form.html")

@app.route('/result', methods = ["GET", "POST"])
def result():
    visID = request.form.get("id")
    date = request.form.get("date")
    time = request.form.get("time")
    direction = request.form.get("direction")
    conn = sqlite3.connect("Task4.db")
    try:
        conn.execute("INSERT INTO Record(Date, Time, Type, visitorId) \
                    VALUES(?, ?, ?, ?)", \
                    (date, time, direction, visID))
        conn.commit()
    except:
        return "Error: Entry not submitted!"
    return render_template("result.html", visID = visID, \
                           date = date, \
                           time = time, \
                           direction = direction)

if __name__ == "__main__":
    app.run(debug=True)
