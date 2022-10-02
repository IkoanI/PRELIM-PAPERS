import sqlite3
conn = sqlite3.connect("equipment.db")

with open("MONITORS.txt") as f:
    for line in f:
        SerialNumber, Model, Location, DateOfPurchase, WrittenOff, DateCleaned = line.strip().split(',')
        conn.execute("INSERT INTO Device VALUES(?, ?, ?, ?, ?, ?)", \
                     (int(SerialNumber), 'Monitor', Model, Location, DateOfPurchase, WrittenOff))

        conn.execute("INSERT INTO Monitor VALUES(?, ?)", \
                     (int(SerialNumber), DateCleaned))

with open("LAPTOPS.txt") as f:
    for line in f:
        SerialNumber, Model, Location, DateOfPurchase, WrittenOff, WeightKg = line.strip().split(',')
        
        conn.execute("INSERT INTO Device VALUES(?, ?, ?, ?, ?, ?)", \
                    (int(SerialNumber), 'Laptop', Model, Location, DateOfPurchase, WrittenOff))

        conn.execute("INSERT INTO Laptop VALUES(?, ?)", \
                    (int(SerialNumber), float(WeightKg)))

with open("PRINTERS.txt") as f:
    for line in f:
        SerialNumber, Model, Location, DateOfPurchase, WrittenOff, Toner, DateChanged = line.strip().split(',')
        conn.execute("INSERT INTO Device VALUES(?, ?, ?, ?, ?, ?)", \
                    (int(SerialNumber), 'Printer', Model, Location, DateOfPurchase, WrittenOff))

        conn.execute("INSERT INTO Printer VALUES(?, ?, ?)", \
                    (int(SerialNumber), Toner, DateChanged))

conn.commit()
conn.close()
