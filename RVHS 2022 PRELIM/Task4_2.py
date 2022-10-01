import sqlite3
conn = sqlite3.connect("invigilation.db")

with open("Teacher.csv") as f:
    for index, line in enumerate(f):
        if index > 0:
            id, name, dept, cont = line.strip().split(',')
            conn.execute("INSERT INTO Teacher VALUES(?, ?, ?, ?)", \
                         (id, name, dept, cont))

with open("Venue.csv") as f:
    for index, line in enumerate(f):
        if index > 0:
            id, name, roomNo = line.strip().split(',')
            conn.execute("INSERT INTO Venue VALUES(?, ?, ?)", \
                         (id, name, roomNo))

with open("ExamSession.csv") as f:
    for index, line in enumerate(f):
        if index > 0:
            sessionID, name, paperNo, venueID, date, start, end = line.strip().split(',')
            conn.execute("INSERT INTO ExamSession VALUES(?, ?, ?, ?, ?, ?, ?)", \
                         (sessionID, name, paperNo, venueID, date, start, end))

with open("ExamDuty.csv") as f:
    for index, line in enumerate(f):
        if index > 0:
            sessionID, teacherID, role = line.strip().split(',')
            conn.execute("INSERT INTO ExamDuty VALUES(?, ?, ?)", \
                         (sessionID, teacherID, role))

conn.commit()
conn.close()
            
