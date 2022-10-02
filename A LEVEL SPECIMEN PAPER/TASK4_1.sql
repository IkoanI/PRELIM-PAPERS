DROP TABLE IF EXISTS `Printer`;
CREATE TABLE IF NOT EXISTS `Printer` (
	`SerialNumber`	INTEGER,
	`Toner`	TEXT,
	`DateChanged`	TEXT,
	PRIMARY KEY(`SerialNumber`),
	FOREIGN KEY(`SerialNumber`) REFERENCES `Device`(`SerialNumber`)
);
DROP TABLE IF EXISTS `Monitor`;
CREATE TABLE IF NOT EXISTS `Monitor` (
	`SerialNumber`	INTEGER,
	`DateCleaned`	TEXT,
	PRIMARY KEY(`SerialNumber`),
	FOREIGN KEY(`SerialNumber`) REFERENCES `Device`(`SerialNumber`)
);
DROP TABLE IF EXISTS `Laptop`;
CREATE TABLE IF NOT EXISTS `Laptop` (
	`SerialNumber`	INTEGER,
	`WeightKg`	REAL,
	PRIMARY KEY(`SerialNumber`),
	FOREIGN KEY(`SerialNumber`) REFERENCES `Device`(`SerialNumber`)
);
DROP TABLE IF EXISTS `Device`;
CREATE TABLE IF NOT EXISTS `Device` (
	`SerialNumber`	INTEGER,
	`Type`	TEXT,
	`Model`	TEXT,
	`Location`	TEXT,
	`DateOfPurchase`	TEXT,
	`WrittenOff`	TEXT,
	PRIMARY KEY(`SerialNumber`)
);
