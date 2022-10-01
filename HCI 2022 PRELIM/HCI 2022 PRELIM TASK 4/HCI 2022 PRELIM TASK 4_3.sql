SELECT Gender, COUNT(Gender), AVG(Weight), AVG(Height)
FROM Student
LEFT JOIN StudentHealthRecord
ON Student.StudentID = StudentHealthRecord.StudentID
GROUP BY Gender;