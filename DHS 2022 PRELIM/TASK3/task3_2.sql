SELECT ballot_result
FROM Results
WHERE nric = "T0663758C";

SELECT "names", y.ballot_result
FROM Results x
JOIN Results y
ON x.group_id = y.group_id
JOIN "Names"
ON "Names".nric = y.nric
WHERE x.nric = "S9981511E"
AND y.nric != "S9981511E"
