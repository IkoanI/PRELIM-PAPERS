import sqlite3
conn = sqlite3.connect("TASK4.DB")
with open("CUSTOMER.TXT") as f:
    data = f.readlines()
    for i in range(1, len(data)):
        Email, FirstName, LastName, ContactNumber, DOB, Address = data[i].strip().split(',')
        conn.execute("INSERT INTO Customer VALUES(?, ?, ?, ?, ?, ?)", \
                     (Email, FirstName, LastName, int(ContactNumber), DOB, Address))

with open("PRODUCT.TXT") as f:
    data = f.readlines()
    for i in range(1, len(data)):
        CatalogueNumber, Category, Brand, Size, Fee = data[i].strip().split(',')
        conn.execute("INSERT INTO Product VALUES(?, ?, ?, ?, ?)", \
                     (int(CatalogueNumber), Category, Brand, int(Size), int(Fee)))

with open("CUSTOMERRENTAL.TXT") as f:
    data = f.readlines()
    for i in range(1, len(data)):
        ID, Email, StartDate, EndDate = data[i].strip().split(',')
        conn.execute("INSERT INTO CustomerRental VALUES(?, ?, ?, ?)", \
                     (int(ID), Email, StartDate, EndDate))

with open("PRODUCTRENTAL.TXT") as f:
    data = f.readlines()
    for i in range(1, len(data)):
        ID, CatalogueNumber, Returned = data[i].strip().split(',')
        conn.execute("INSERT INTO ProductRental VALUES(?, ?, ?)", \
                     (int(ID), int(CatalogueNumber), Returned))

conn.commit()
conn.close()
