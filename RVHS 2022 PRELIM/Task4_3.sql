SELECT Teacher.Name, ExamSession.SubjectName, ExamSession.PaperNo, ExamDuty.'Role', Venue.VenueName, ExamSession.'Date', ExamSession.StartTime, ExamSession.EndTime
FROM ExamDuty, ExamSession, Venue, Teacher
WHERE ExamDuty.TeacherID = Teacher.TeacherID
AND ExamSession.ExamSessionID = ExamDuty.ExamSessionID
AND Venue.VenueID = ExamSession.VenueID
ORDER BY ExamSession.'Date', ExamSession.StartTime ASC;
