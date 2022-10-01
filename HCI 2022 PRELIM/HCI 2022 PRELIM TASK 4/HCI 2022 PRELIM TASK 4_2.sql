SELECT Name, Gender, Weight, Height
FROM Student
LEFT JOIN StudentHealthRecord
ON Student.StudentID = StudentHealthRecord.StudentID
ORDER BY Student.Gender ASC, Student.Name DESC