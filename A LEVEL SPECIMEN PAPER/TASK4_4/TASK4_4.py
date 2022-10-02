from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/')
def form():
    return render_template("form.html")

@app.route('/display', methods = ["POST"])
def display():
    location = request.form.get("location")
    conn = sqlite3.connect("equipment.db")
    data = conn.execute("SELECT SerialNumber, Type " +
                        "FROM Device " +
                        f"WHERE Location = '{location}' " +
                        "AND WrittenOff = 'FALSE'").fetchall()
    conn.close()
    return render_template("display.html", data = data)

if __name__ == "__main__":
    app.run(debug = True)
