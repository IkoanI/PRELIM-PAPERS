from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/')
def menu():
    return render_template("menu.html")

@app.route('/insert')
def insert():
    return render_template("insert.html")

@app.route('/result', methods = ["GET", "POST"])
def result():
    bookID = request.form.get("bookID")
    title = request.form.get("title")
    price = request.form.get("price")
    copies = request.form.get("copies")
    conn = sqlite3.connect("Task4.db")

    try:
        conn.execute("INSERT INTO books VALUES(?, ?, ?)", \
                    (bookID, title, float(price)))
        conn.commit()

    except:
        pass

    try:
        for i in range(int(copies)):
            count = conn.execute(f"SELECT COUNT(copyID) FROM copies \
                                WHERE bookID == {bookID}").fetchone()[0]
            currentCount = str(int(count) + 1)

            copyID = ""
            for j in range(4):
                if j > len(currentCount) - 1:
                    copyID += '0'
                else:
                    copyID += currentCount[::-1][j]

            conn.execute("INSERT INTO copies VALUES(?, ?)", \
                         (copyID[::-1], bookID))
            conn.commit()

        conn.close()
        return render_template("result.html", \
                               message = "Inserted successfully!")

    except:
        conn.close()
        return render_template("result.html", \
                               message = "Not inserted successfully!")

@app.route('/display')
def display():
    conn = sqlite3.connect("Task4.db")
    books = conn.execute("SELECT * FROM books ORDER BY title ASC").fetchall()
    newBooks = []
    for book in books:
        bookID = book[0]
        title = book[1]
        price = book[2]
        count = conn.execute(f"SELECT COUNT(copyID) FROM copies \
                                WHERE bookID == '{bookID}'").fetchone()[0]
        newBooks.append([bookID, title, price, count])
        
    return render_template("display.html", books = newBooks)

if __name__ == "__main__":
    app.run(debug = True)
