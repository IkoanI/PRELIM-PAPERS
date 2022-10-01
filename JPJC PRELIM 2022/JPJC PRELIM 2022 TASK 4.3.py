from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)
custEmail = ""

@app.route('/', methods = ["POST", "GET"])
def index():
    global custEmail
    if request.method == "POST":
        conn= sqlite3.connect("TASK4.db")
        email = request.form.get("email")
        result = conn.execute(f"SELECT COUNT(Email) FROM Customer WHERE Email = '{email}'").fetchone()
        conn.close()
        if result[0] == 1:
            return render_template("index.html", noEmail = True, invalidEmail = True)
        else:
            custEmail = email
            return render_template("index.html", noEmail = False, invalidEmail = False)
    return render_template("index.html", noEmail = True, invalidEmail = False)

@app.route('/success', methods = ["POST", "GET"])
def success():
    global custEmail
    fname = request.form.get("fname")
    lname = request.form.get("lname")
    contact = request.form.get("contact")
    dob = request.form.get("dob")
    addr = request.form.get("addr")
    conn= sqlite3.connect("TASK4.db")
    conn.execute("INSERT INTO Customer VALUES(?, ?, ?, ?, ?, ?)", \
                 (custEmail, fname, lname, contact, dob, addr))
    conn.commit()
    conn.close()
    return render_template("success.html")


if __name__ == "__main__":
    app.run(debug = True, port = 5678)
