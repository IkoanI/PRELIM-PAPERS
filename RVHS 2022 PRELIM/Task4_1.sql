DROP TABLE IF EXISTS `Venue`;
CREATE TABLE IF NOT EXISTS `Venue` (
	`VenueID`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`VenueName`	TEXT,
	`RoomNo`	INTEGER
);
DROP TABLE IF EXISTS `Teacher`;
CREATE TABLE IF NOT EXISTS `Teacher` (
	`TeacherID`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`Name`	TEXT,
	`Department`	TEXT,
	`Contact`	INTEGER
);
DROP TABLE IF EXISTS `ExamSession`;
CREATE TABLE IF NOT EXISTS `ExamSession` (
	`ExamSessionID`	INTEGER,
	`SubjectName`	TEXT,
	`PaperNo`	INTEGER,
	`VenueID`	INTEGER,
	`Date`	TEXT,
	`StartTime`	TEXT,
	`EndTime`	TEXT,
	FOREIGN KEY(`VenueID`) REFERENCES `Venue`(`VenueID`),
	PRIMARY KEY(`ExamSessionID`)
);
DROP TABLE IF EXISTS `ExamDuty`;
CREATE TABLE IF NOT EXISTS `ExamDuty` (
	`ExamSessionID`	INTEGER,
	`TeacherID`	INTEGER,
	`Role`	TEXT CHECK(Role IN ( 'PaperCoordinator' , 'Invigilator' , 'Relief' , 'RestroomDuty' , 'Reserve' )),
	FOREIGN KEY(`ExamSessionID`) REFERENCES `ExamSession`(`ExamSessionID`),
	PRIMARY KEY(`ExamSessionID`,`TeacherID`),
	FOREIGN KEY(`TeacherID`) REFERENCES `Teacher`(`TeacherID`)
);
