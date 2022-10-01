import sqlite3
conn = sqlite3.connect("invigilation.db")
teachers = conn.execute("SELECT Name FROM Teacher ORDER BY Name ASC").fetchall()
result = []
for teacher in teachers:
    roles = conn.execute("SELECT DISTINCT ExamDuty.'Role' " +
                         "FROM ExamDuty, Teacher " +
                         f"WHERE Teacher.Name = '{teacher[0]}' " +
                         "AND ExamDuty.TeacherID = Teacher.TeacherID " +
                         "ORDER BY ExamDuty.'Role' ASC").fetchall()
    for role in roles:
        count = conn.execute("SELECT COUNT(ExamDuty.Role) " +
                             "FROM ExamDuty, Teacher " +
                             f"WHERE Teacher.Name = '{teacher[0]}' " +
                             "AND ExamDuty.TeacherID = Teacher.TeacherID " +
                             f"AND ExamDuty.'Role' = '{role[0]}'").fetchone()

        result.append([teacher[0], role[0], count[0]])
                      
    
print(result)
