SELECT SUM(Equipment.Points)
FROM Loan
INNER JOIN Equipment
ON Equipment.ID = Loan.EqptID
INNER JOIN Student
ON Loan.StudentID = Student.ID
WHERE Student.Name = "Andy";

SELECT Student.Name, SUM(Equipment.Points)
FROM Loan
INNER JOIN Student
ON Loan.StudentID = Student.ID
INNER JOIN Equipment
ON Loan.EqptID = Equipment.ID
GROUP BY Student.Name
ORDER BY SUM(Equipment.Points) DESC
LIMIT 3;