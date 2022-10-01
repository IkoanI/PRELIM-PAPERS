SELECT Name, Time FROM Person, Record
WHERE Type = 'entry' AND Time > '0730'
ORDER BY record.Date ASC;