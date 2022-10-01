import sqlite3

conn = sqlite3.connect("Task4.db")
with open("books_data.txt") as f:
    data = f.readlines()
    for row in data:
        bookID, title, price = row.strip().split(',')
        conn.execute("INSERT INTO books VALUES(?, ?, ?)", \
                     (bookID, title, price))

with open("copies_data.txt") as f:
    data = f.readlines()
    for row in data:
        copyID, bookID, title, price = row.strip().split(',')
        conn.execute("INSERT INTO copies VALUES(?, ?)", \
                     (copyID, bookID))

conn.commit()
conn.close()
