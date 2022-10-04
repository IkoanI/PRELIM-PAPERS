import os, sqlite3
from flask import Flask, render_template, request, send_from_directory
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/upload', methods = ["GET", "POST"])
def upload():
    if request.method == "POST" and request.files and "photo" in request.files:
        name = request.form.get("name")
        photo = request.files["photo"]
        filename = secure_filename(photo.filename)
        path = os.path.join('uploads', filename)
        photo.save(path)

        conn = sqlite3.connect("Photos.db")
        conn.execute("INSERT INTO Photos VALUES(?, ?)", (name, filename))
        conn.commit()
        conn.close()
        return render_template("home.html")

    return render_template("upload.html")

@app.route('/view', methods = ["GET", "POST"])
def view():
    if request.method == "POST":
        name = request.form.get("name")
        conn = sqlite3.connect("Photos.db")
        filename = conn.execute(f"SELECT Photo FROM Photos WHERE Name = '{name}'").fetchone()
        return render_template("view.html", noName = False, filename = filename[0])
    return render_template("view.html", noName = True)

@app.route('/photo/<filename>')
def get_photo(filename):
    return send_from_directory('uploads', filename)
    

app.run(debug = True)
