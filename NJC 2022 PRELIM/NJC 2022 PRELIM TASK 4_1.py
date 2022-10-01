import sqlite3

with open("TIDES.TXT") as f:
    data = [line.strip().split("\t") for line in f]

conn = sqlite3.connect("tide.db")
for row in data:
    Date, Time, isHigh, Height = row
    if isHigh == "LOW":
        isHigh = 0
    else:
        isHigh = 1

    conn.execute("INSERT INTO Tide(Date, Time, isHigh, Height) " +
                 "VALUES(?, ?, ?, ?)", (Date, Time, isHigh, float(Height)))

conn.commit()
conn.close()
    
