USE Ticketing;




-- CREATE TABLE Subscriber(
--     Email char(50) NOT NULL,
-- 	   Name char(50),
--     DOB DATETIME,
--     Gender char(1),
--     PRIMARY KEY (Email)
-- );


-- CREATE TABLE Flight(
--     FlightID int NOT NULL AUTO_INCREMENT,
--     Email char(50) NOT NULL,
-- 	Arrival char(50),
--     Departure char(50),
--     Date DATETIME,
-- 	PRIMARY KEY (FlightID),
--     FOREIGN KEY (Email) REFERENCES Subscriber(Email)
-- );

-- CREATE TABLE FlightDetail(
--     FlightDetailID int NOT NULL AUTO_INCREMENT,
--     FlightID int NOT NULL,
--     Airline char(30),
-- 	   Time char(30),
--     Price int,
-- 	   PRIMARY KEY (FlightDetailID),
--     FOREIGN KEY (FlightID) REFERENCES Flight(FlightID)
-- );


#SELECT LAST_INSERT_ID();
#DELETE FROM flight WHERE Email = "papi@yahoo.com";
#DELETE FROM Subscriber WHERE Email = "papi@yahoo.com";
#select * from Subscriber;
#select * from flight;
#select * from flightDetail;

-- SELECT * FROM Ticketing.Subscriber s , Ticketing.Flight f ,Ticketing.FlightDetail fd
-- where s.Email = f.Email and f.FlightID = fd.FlightID;












