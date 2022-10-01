BEGIN TRANSACTION;
DROP TABLE IF EXISTS `ProductRental`;
CREATE TABLE IF NOT EXISTS `ProductRental` (
	`ID`	INTEGER,
	`CatalogueNumber`	INTEGER,
	`Returned`	TEXT,
	FOREIGN KEY(`CatalogueNumber`) REFERENCES `Product`(`CatalogueNumber`),
	PRIMARY KEY(`ID`,`CatalogueNumber`),
	FOREIGN KEY(`ID`) REFERENCES `CustomerRental`(`ID`)
);
DROP TABLE IF EXISTS `Product`;
CREATE TABLE IF NOT EXISTS `Product` (
	`CatalogueNumber`	INTEGER,
	`Category`	TEXT,
	`Brand`	TEXT,
	`Size`	INTEGER,
	`Fee`	INTEGER,
	PRIMARY KEY(`CatalogueNumber`)
);
DROP TABLE IF EXISTS `CustomerRental`;
CREATE TABLE IF NOT EXISTS `CustomerRental` (
	`ID`	INTEGER,
	`Email`	TEXT,
	`StartDate`	TEXT,
	`EndDate`	TEXT,
	PRIMARY KEY(`ID`),
	FOREIGN KEY(`Email`) REFERENCES `Customer`(`Email`)
);
DROP TABLE IF EXISTS `Customer`;
CREATE TABLE IF NOT EXISTS `Customer` (
	`Email`	TEXT,
	`FirstName`	TEXT,
	`LastName`	TEXT,
	`ContactNumber`	INTEGER,
	`DOB`	TEXT,
	`Address`	INTEGER,
	PRIMARY KEY(`Email`)
);
COMMIT;
