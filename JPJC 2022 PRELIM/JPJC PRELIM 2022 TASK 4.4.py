from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("rentalsdue.html")

@app.route('/result', methods = ["GET", "POST"])
def result():
    endDate = request.form.get("endDate")
    conn = sqlite3.connect("TASK4.db")
    result = conn.execute("SELECT ProductRental.ID, ProductRental.CatalogueNumber, " +
                 "Customer.Email, Customer.ContactNumber " +
                 "FROM ProductRental, Customer, CustomerRental " +
                 f"WHERE CustomerRental.EndDate = '{endDate}' " +
                 "AND Customer.Email = CustomerRental.Email " +
                 "AND ProductRental.ID = CustomerRental.ID " +
                 "AND ProductRental.Returned = 'FALSE'").fetchall()
    
    return render_template("result.html", result = result)

if __name__ == "__main__":
    app.run(debug = True, port = 5000)
