import sqlite3
conn = sqlite3.connect("SportsLoans.db")

with open("Loan.TXT") as f:
    next(f)
    for line in f:
        LoanId, EqptID, StudentID, LoanDate, ReturnDate = line.strip().split(',')
        conn.execute("INSERT INTO Loan VALUES(?, ?, ?, ?, ?)", \
                     (LoanId, EqptID, StudentID, LoanDate, ReturnDate))

    conn.commit()
    conn.close()
