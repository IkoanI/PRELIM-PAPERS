from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/dashboard', methods = ["GET", "POST"])
def dashboard():
    nric = request.form.get("nric")
    conn = sqlite3.connect("ballot.db")
    yourResult = conn.execute("SELECT ballot_result " +
                              "FROM Results " +
                              f"WHERE nric = '{nric}'").fetchone()
    
    result = conn.execute("SELECT names, y.ballot_result " +
                          "FROM Results x " +
                          "JOIN Results y " +
                          "ON x.group_id = y.group_id " +
                          "JOIN Names " +
                          "ON Names.nric = y.nric " +
                          f"WHERE x.nric = '{nric}' " +
                          f"AND y.nric != '{nric}'").fetchall()
    
    return render_template("dashboard.html", yourResult = yourResult, result = result)

if __name__ == "__main__":
    app.run(debug = True)
