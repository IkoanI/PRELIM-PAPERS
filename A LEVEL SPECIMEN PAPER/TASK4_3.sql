SELECT Device.SerialNumber, Model, Location, DateCleaned
FROM Device
INNER JOIN Monitor
ON Device.SerialNumber = Monitor.SerialNumber;